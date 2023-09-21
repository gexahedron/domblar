( // init
s.options.sampleRate = 48000;
s.options.memSize = 8192 * 64; // increase this if you get "alloc failed" messages
s.options.maxNodes = 1024 * 32; // increase this if you are getting drop outs and the message "too many nodes"
s.options.numBuffers = 1024 * 16;

// for live-coding streaming
// s.options.outDevice_("BlackHole 2ch");

s.options.numOutputBusChannels = 2;
s.options.numInputBusChannels = 2;

s.latency = 0.2;

s.boot();

s.waitForBoot({
	("vst_utils.scd").loadRelative;
});
StageLimiter.activate;
)


Server.killAll; // also callable from Python with "d = Domblar(...); d.stop_server()"









~controllers[0].editor;


n = NetAddr.new("127.0.0.1", 7771);

(
~controllers[0].numParameters.do { arg i;
	// i.post;
	// " ".post;
	// ~controllers[0].info.parameters[i].name.postln;
	n.sendMsg("/params", ~controllers[0].info.parameters[i].name);
}
)

FoxDot.start;
a = Synth(\glissando);

// nice filters
{ |ffreq=390| RLPFD.ar(Mix(LFSaw.ar([120, 180], 0, 0.33)), LinExp.kr(LFCub.kr(0.1, 0.5*pi), -1, 1, 280, 1500), 0.6, 0.0, mul:3.0).dup }.play
{ |ffreq=390| MoogVCF.ar(Mix(LFSaw.ar([120, 180], 0, 0.33)), LinExp.kr(LFCub.kr(0.1, 0.5*pi), -1, 1, 280, 1500), 0.75, 2.0).dup }.play
{BLowPass4.ar(Mix(LFSaw.ar([120, 180], mul:0.2)), LinExp.kr(LFCub.kr(0.1, 0.5*pi), -1, 1, 280, 1500), 0.2).dup }.play
{BLowPass.ar(Mix(LFSaw.ar([120, 180], mul:0.2)), LinExp.kr(LFCub.kr(0.1, 0.5*pi), -1, 1, 280, 1500), 0.2).dup }.play
(
{
    NLFiltC.ar(
        LFSaw.ar([120, 180], 0, mul:0.1),
        0.5,
        -0.04,
        0.8,
        0.2,
        LFCub.kr(0.2, [0, 0.5 * pi], 63, 103)
    )
}.play
)
{ Streson.ar(LFSaw.ar([220, 180], 0, mul:EnvGen.kr(Env.asr(0.5, 1, 0.02), 1.0) * 0.2), LinExp.kr(LFCub.kr(0.1, 0.5*pi), -1, 1, 280, 377).reciprocal, 0.9, 0.3) }.play

FoxDot.start;

// StageMaster.activate(numChannels: 2, compThreshold: 0.7, limiterLevel: 1.0, highEndDb: 3.0);
// StageMaster.deactivate;

// TODO:
// sending OSC from SuperCollider
// https://doc.sccode.org/Guides/OSC_communication.html

// TODO:
// print all parameter names
// (
// ~controllers[0].numParameters.do { arg i;
// 	i.post;
// 	" ".post;
// 	~controllers[0].info.parameters[i].name.postln;
// }
// )


( // init
s.options.sampleRate = 48000;
s.options.memSize = 8192 * 64; // increase this if you get "alloc failed" messages
s.options.maxNodes = 1024 * 32; // increase this if you are getting drop outs and the message "too many nodes"
s.options.numBuffers = 1024 * 16;

// for live-coding streaming
// s.options.outDevice_("BlackHole 2ch");

s.options.numOutputBusChannels = 2;
s.options.numInputBusChannels = 2;

s.latency = 0.2;

s.boot();
)

VSTPlugin.clear();
VSTPlugin.search();

(
SynthDef(\vst_plugin, {|
	out, gate = 1,
	mix = 0.25, room = 0.7, damp = 0.5,
	dur = 1.0, amp = 1.0|
	// FIXME: i think the envelope is useless atm
	var env = Env.adsr(
		attackTime: 0.0,
		decayTime: 0.0,
		sustainLevel: dur * 0.9,
		releaseTime: dur * 0.1);
    var gen = EnvGen.kr(env, gate, doneAction: Done.freeSelf);
	var sig = VSTPlugin.ar(numOut: 2) * amp;
	sig = FreeVerb.ar(sig, mix, room, damp);
	Out.ar(out, sig * gen);
}).add;
)

~synth = Synth(\vst_plugin);
~fx = VSTPluginController(~synth);
/*~fx.open('Dexed.vst3');*/
/*~fx.open('chipsynth OPS7.vst3');*/
// ~fx.open('TripleCheese.vst3');
// ~fx.open('TyrellN6.vst');
~fx.open('OPL.vst');
~fx.editor;
~fx.gui;

(
~ctl = Bus.control;
~lfo = {Out.kr(~ctl, LFTri.kr(0.2, 0, 0.5, 0.5))}.play;
~ctl2 = Bus.control;
~lfo2 = {Out.kr(~ctl2, LFTri.kr(0.1, 0.3, 0.5, 0.5))}.play;
~ctl3 = Bus.control;
~lfo3 = {Out.kr(~ctl3, LFTri.kr(0.5, 0.6, 0.5, 0.5))}.play;
)

~fx.loadPreset('dexed_preset');
~fx.midi.noteOn(0, 60, 127);
~fx.midi.bend(0, 8192);
~fx.midi.noteOn(0, 61, 127);
a = Task.new({ loop({ ~fx.midi.noteOn(0, 60, 127); 1.wait; }) });
a.play;
a.stop;
~fx.midi.noteOff(0, 60, 127);
~fx.midi.noteOff(0, 61, 127);

~fx.map(15, ~ctl3);
~fx.map(91, ~ctl3);
~fx.map(60, ~ctl3);
~fx.map(84, ~ctl3);
~fx.map(53, ~ctl2);
~fx.unmap(10);
// ~fx.map(122, ~ctl);
// ~fx.map(120, ~ctl2);
// ~fx.map(99, ~ctl);
// ~fx.map(77, ~ctl2);
// ~fx.map(75, ~ctl);
// ~fx.map(95, ~ctl2);
// ~fx.map(118, ~ctl3);
// 1 - volume?
// 9 - tremolo
// 29, 32, 33spectral, 34
// 51, 53, 54
// 73, 75!, 76?!, 77spectral, 78, 81+82
// 95!, 99spectral, 100+..+107
// 118, +120, 122spectral, +129
// 138/139 breaks;
~fx.midi.noteOff(0, 60, 127);


SynthDef.new(\eeri,{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, blur=1, cutoff=400, beat_dur=1, atk=0.01, decay=0.01, rel=0.01, peak=1, level=0.8|var osc, env;sus = sus * blur;freq = In.kr(bus, 1);freq = [freq, freq+fmod];sus=(sus * 1.75);amp=(amp*2);freq=Vibrato.kr(freq, (rate + 4));osc = 	 RLPF.ar(SinOsc.ar(Saw.ar([1, 2]).range(1, 104)) * SyncSaw.ar(SinOsc.ar(0.01).range(1, 100), SinOsc.ar(0.01).range(freq, freq*2)), Line.ar(cutoff, freq, 1));osc = 	GVerb.ar(osc + CombL.ar(osc, 0.3, 1, 1), 10);env=EnvGen.ar(Env(times: [(sus / 2), (sus / 2)],levels: [0, amp, 0],curve: 'lin'), doneAction: 0);osc=(osc * env);osc = Mix(osc) * 1/16;osc = Pan2.ar(osc, pan);	ReplaceOut.ar(bus, osc)}).add;

