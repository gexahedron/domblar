(
SynthDef(\vst_plugin, {|out, gate = 1, mix = 0.25, room = 0.15, damp = 0.5|
	var sig = VSTPlugin.ar(numOut: 2);
	// var sig = VSTPlugin.ar(Silent.ar, numOut: 2);
	sig = FreeVerb.ar(sig, mix, room, damp);
	Out.ar(out, sig);
}).add;

f.free;
f = OSCFunc({ |msg, time, addr, port|
	var synth_idx = msg[1];
	var note = msg[2];
	var bend = msg[3];
	var dur = msg[4];
	// var chan = 2; // MPE
	var chan = 2 + msg[5];

	SystemClock.sched(time - Main.elapsedTime, {
		p = Pbind(
			\type, \vst_midi,
			\vst, c[synth_idx],
			\midinote, Pseq([note]),
			\chan, chan,
			\dur, Pseq([dur*0.9]),
			\amp, 1.0
		);

		q = Pbind(
			\type, \vst_midi,
			\vst, c[synth_idx],
			\midicmd, \bend,
			\val, Pseq([bend]), // def 8192, min 0, max 16383
			\chan, chan,
			\dur, Pseq([dur*0.9]),
		);

		r = Ppar([q, p]).play;
	});
}, "/tracker");

z.free;
z = OSCFunc({ |msg, time, addr, port|
	var synth_idx = msg[1];
	var shift = msg[2];
	var params = msg[3..];
	synth_idx.postln;
	params.postln;
	c[synth_idx].setn(shift, params);
}, "/set_instrument");

y.free;
y = OSCFunc({ |msg, time, addr, port|
	s.record;
}, "/record");

x.free;
x = OSCFunc({ |msg, time, addr, port|
	s.stopRecording;
}, "/stop_recording");

)