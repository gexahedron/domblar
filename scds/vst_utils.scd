(
//// synthdefs ////
SynthDef(\vst_plugin, {|out, gate = 1, mix = 0.25, room = 0.15, damp = 0.5, dur = 1.0, amp = 1.0|
	var env = Env.adsr(
		attackTime: 0.000,
		decayTime: 0.0,
		sustainLevel: dur * 0.9,
		releaseTime: dur * 0.1);
    var gen = EnvGen.kr(env, gate, doneAction: Done.freeSelf);
	var sig = VSTPlugin.ar(numOut: 2) * amp;
	// var sig = VSTPlugin.ar(Silent.ar, numOut: 2);
	sig = FreeVerb.ar(sig, mix, room, damp);
	Out.ar(out, sig * gen);
}).add;


//// functions ////
~vst_setup_func.free;
~vst_setup_func = OSCFunc({ |msg, time, addr, port|
	var synth_count = msg[1];
	var synth_names = msg[2..];
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
	~controllers[synth_idx].setn(shift, params);
}, "/set_instrument");

~play_func.free;
~play_func = OSCFunc({ |msg, time, addr, port|
	var synth_idx = msg[1];
	var note = msg[2];
	var bend = msg[3];
	var dur = msg[4];
	var amp = msg[5];
	var chan = msg[6];

	/*SystemClock.sched(time - Main.elapsedTime, {
		p = Pbind(
			\type, \vst_midi,
			\vst, ~controllers[synth_idx],
			\midinote, Pseq([note]),
			\chan, chan,
			\dur, Pseq([dur]),
			\amp, amp / 127
		);

		q = Pbind(
			\type, \vst_midi,
			\vst, ~controllers[synth_idx],
			\midicmd, \bend,
			\val, Pseq([bend]),
			\chan, chan,
			\dur, Pseq([dur]),
		);

		r = Ppar([q, p]).play;
	});*/

	SystemClock.sched(time - Main.elapsedTime, {
		s.bind {
			~controllers[synth_idx].midi.noteOn(chan, note, 127);
			~controllers[synth_idx].midi.bend(chan, bend);
			~synths[synth_idx].set(\dur, dur);
			~synths[synth_idx].set(\amp, amp / 127);
		};
	});
	SystemClock.sched(time + dur - Main.elapsedTime, {
		s.bind {
			~controllers[synth_idx].midi.noteOff(chan, note);
		};
	});
}, "/play");


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