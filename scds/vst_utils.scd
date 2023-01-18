(
//// synthdefs ////
SynthDef(\vst_plugin, {|out, gate = 1, mix = 0.25, room = 0.15, damp = 0.5|
	var sig = VSTPlugin.ar(numOut: 2);
	// var sig = VSTPlugin.ar(Silent.ar, numOut: 2);
	sig = FreeVerb.ar(sig, mix, room, damp);
	Out.ar(out, sig);
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
	var preset = msg[2];
	~controllers[synth_idx].getn(0, -1, action: {arg v; Post << v});
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
	var chan = msg[5];
	// TODO: add amp

	SystemClock.sched(time - Main.elapsedTime, {
		p = Pbind(
			\type, \vst_midi,
			\vst, ~controllers[synth_idx],
			\midinote, Pseq([note]),
			\chan, chan,
			\dur, Pseq([dur]),
			\amp, 1.0
		);

		q = Pbind(
			\type, \vst_midi,
			\vst, ~controllers[synth_idx],
			\midicmd, \bend,
			\val, Pseq([bend]), // def 8192, min 0, max 16383
			\chan, chan,
			\dur, Pseq([dur]),
		);

		r = Ppar([q, p]).play;
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