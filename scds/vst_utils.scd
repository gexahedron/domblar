(
//// constants ////
~quant_steps = 127;

//// synthdefs ////
SynthDef(\vst_plugin, {|
	out,
	gate=1,
	dur=1.0, amp=1.0, pan=0.0,
	mix=0.25, room=0.7, damp=0.5,
	lpf=20000.0, lpr=1.0|
	// FIXME: i think the envelope is useless atm
	// var env = Env.adsr(
	// 	attackTime: 0.0,
	// 	decayTime: 0.0,
	// 	sustainLevel: dur * 0.9,
	// releaseTime: dur * 0.1);
	// var gen = EnvGen.kr(env, gate, doneAction: Done.freeSelf);
	var osc = VSTPlugin.ar(numOut: 1) * amp;
	osc = FreeVerb.ar(osc, mix, room, damp);
	osc = RLPF.ar(osc, lpf, lpr);
	osc = Pan2.ar(osc, pan);
	// Out.ar(out, osc * gen);
	Out.ar(out, osc);
}).add;

// TODO:
// SynthDef.new(\lowPassFilter, {|bus, lpf, lpr|
// 	var osc;
// 	osc = In.ar(bus, 2);
// 	osc = RLPF.ar(osc, lpf, lpr);
// 	ReplaceOut.ar(bus, osc);
// }).add;


//// functions ////
~vst_setup_func.free;
~vst_setup_func = OSCFunc({ |msg, time, addr, port|
	var synth_count = msg[1];
	var synth_names = msg[2..];

	// cleaning stuff
	~synth_count.do { arg i;
		~synths[i].free;
		~controllers[i].free;
	};

	~synth_count = synth_count;
	~synths = Array.fill(synth_count, nil);
	~controllers = Array.fill(synth_count, nil);

	synth_count.do { arg i;
		~synths[i] = Synth(\vst_plugin);
		~controllers[i] = VSTPluginController(~synths[i]);
		~controllers[i].open(synth_names[i]);
	};
}, "/vst_setup");

// useful for resetting Mono mode for Dexed
// or for loading synth parameters
~load_preset_func.free;
~load_preset_func = OSCFunc({ |msg, time, addr, port|
	var synth_idx = msg[1];
	var preset = msg[2];
	~controllers[synth_idx].loadPreset(preset);
}, "/load_preset");

// useful for saving synth parameters
~save_preset_func.free;
~save_preset_func = OSCFunc({ |msg, time, addr, port|
	var synth_idx = msg[1];
	var preset = msg[2];
	~controllers[synth_idx].savePreset(preset);
}, "/save_preset");

// useful for saving synth parameters
~print_params_func.free;
~print_params_func = OSCFunc({ |msg, time, addr, port|
	var synth_idx = msg[1];
	~controllers[synth_idx].getn(0, -1, action: {arg v; Post << v});
	"".postln;
}, "/print_params");

// useful for tinkering with synth parameters
~open_editor_func.free;
~open_editor_func = OSCFunc({ |msg, time, addr, port|
	var synth_idx = msg[1];
	~controllers[synth_idx].editor;
}, "/open_editor");

~set_instrument_func.free;
~set_instrument_func = OSCFunc({ |msg, time, addr, port|
	var synth_idx = msg[1];
	var shift = msg[2];
	var params = msg[3..];
	SystemClock.sched(time - Main.elapsedTime, {
		s.bind {
			 ~controllers[synth_idx].setn(shift, params);
		};
	});
}, "/set_instrument");

~set_param.free;
~set_param = OSCFunc({ |msg, time, addr, port|
	var synth_idx = msg[1];
	var param = msg[2];
	var val = msg[3];
	~synths[synth_idx].set(param, val / ~quant_steps);
}, "/set_param");

~play_func.free;
~play_func = OSCFunc({ |msg, time, addr, port|
	var synth_idx = msg[1];
	var note = msg[2];
	var bend = msg[3];
	var dur = msg[4];
	var amp = msg[5];
	var chan = msg[6];
	var state = msg[7];
	var pan = msg[8];
	var mix = msg[9];
	var lpf = msg[10];
	var lpr = msg[11];

	// state == 0: usual note
	// state == 1: drone, midi.noteOn
	// state == 2: drone, midi.noteOff
	if ( state <= 1,
		{
			SystemClock.sched(time - Main.elapsedTime, {
				s.bind {
					~controllers[synth_idx].midi.bend(chan, bend);
					~controllers[synth_idx].midi.noteOn(chan, note, ~quant_steps);
					~synths[synth_idx].set(\dur, dur);
					~synths[synth_idx].set(\amp, amp / ~quant_steps);
					~synths[synth_idx].set(\pan, pan / ~quant_steps);
					~synths[synth_idx].set(\mix, mix / ~quant_steps);
					~synths[synth_idx].set(\lpf, lpf / ~quant_steps);
					~synths[synth_idx].set(\lpr, lpr / ~quant_steps);
				};
			});
		},
		{}
	);
	if ( state == 0,
		{
			SystemClock.sched(time + dur - Main.elapsedTime, {
				s.bind {
					~controllers[synth_idx].midi.noteOff(chan, note);
				};
			});
		},
		{}
	);
	// used for drones
	if ( state == 2,
		{
			SystemClock.sched(time - Main.elapsedTime, {
				s.bind {
					~controllers[synth_idx].midi.noteOff(chan, note);
				};
			});
		},
		{}
	);
}, "/play");

~modify_func.free;
~modify_func = OSCFunc({ |msg, time, addr, port|
	var synth_idx = msg[1];
	var chan = msg[2];
	var lpf = msg[3];
	var lpr = msg[4];

	SystemClock.sched(time - Main.elapsedTime, {
		s.bind {
			~synths[synth_idx].set(\lpf, lpf / ~quant_steps);
			~synths[synth_idx].set(\lpr, lpr / ~quant_steps);
		};
	});
}, "/modify");

~record_func.free;
~record_func = OSCFunc({ |msg, time, addr, port|
	s.record;
}, "/record");

~stop_recording_func.free;
~stop_recording_func = OSCFunc({ |msg, time, addr, port|
	s.stopRecording;
}, "/stop_recording");

~stop_server_func.free;
~stop_server_func = OSCFunc({ |msg, time, addr, port|
	Server.killAll;
}, "/stop_server");

)