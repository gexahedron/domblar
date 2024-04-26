(SynthDef(\fmBass, {
	arg
	//Standard Values
	out = 0, pan = 0, amp = 0.1, freq = 150, att = 0.0005, rel = 1, crv = -3,
	// Other Controls
	attFraction = 0.05, relFraction = 0.7, modIndex = 500, modRatio = 1.51,
	subAmp = 0.75, modFB = 0.4;

	var scale, mAtt, mRel, modulatorEnv, modulator, carrierEnv, carrier, snd;

	// Scale the att/rel for the Modulator
	scale = (attFraction + relFraction);
	scale = Select.kr(
		which: InRange.kr(
			in: scale,
			lo: 1,
			hi: inf),
		array: [
			DC.kr([attFraction, relFraction]),
			DC.kr([attFraction/scale, relFraction/scale])
	]);
	scale = scale * (att + rel);

	mAtt = scale[0];
	mRel = scale[1];

	// Modulator
	modulatorEnv = Env.perc(
		attackTime: mAtt,
		releaseTime: mRel,
		level: modIndex,
		curve: crv).ar;
	modulator = SinOscFB.ar(
		freq: freq * modRatio,
		feedback: modFB,
		mul: modulatorEnv);

	// Carrier
	carrierEnv = Env.perc(
		attackTime: att,
		releaseTime: rel,
		curve: crv).ar(doneAction: 2);
	carrier = SinOsc.ar(
		freq: freq + modulator,
		mul: carrierEnv);

    // Add a Sub
	snd = carrier + SinOsc.ar(
		freq: freq/2,
		mul: carrierEnv * subAmp);

	// Output Stuff
	snd = snd * amp;
	snd = Limiter.ar(snd);

	Out.ar(out, Pan2.ar(snd));
},
metadata: (
	credit: "Josh Mitchell",
	category: \bass,
	tags: [\pitched, \fm]
	)
).add;)



(
Pbindef( \fmBass,
	\instrument, "fmBass",
	\ctranspose, -15,
	\attFraction, Pwhite(0.05, 0.15),
	\relFraction, Pwhite(0.2, 0.75),
	\modIndex, Pwhite(600, 800),
	\subAmp, Pseq([
		1, 0.5, 0.5, 0.5, 0.5,
		1, 0.5, 0.5, 0.5, 0.5, 0.5,
		1, 0.5, 0.5, 0.5, 1.5, 0.5,
		1, 0.5, 0.5,
		1, 0.5, 0.5, 0.5, 0.5,
		1, 0.5, 0.5, 0.5, 0.5, 0.5,
		1, 0.5, 0.5, 0.5, 0.5, 0.5,
		1, 0.5, 0.5, 0.5
	]),
	\rel, Pseq([
		0.5, 0.5, 0.5, 0.5, 1,
		0.5, 0.5, 0.5, 0.5, 0.5, 1,
		0.5, 0.5, 0.5, 0.5, 1.5, 0.5,
		0.25, 0.25, 1,
		0.5, 0.5, 0.5, 0.5, 1,
		0.5, 0.5, 0.5, 0.5, 0.5, 1,
		0.5, 0.5, 0.5, 0.5, 1.5, 0.5,
		0.25, 0.25, 1, 2
	]),
	\dur, Pseq([
		1/8, 1/8, 1/4, 1/8, 3/8,
		1/4, 1/8, 1/8, 1/8, 1/8, 1/4,
		1/8, 1/8, 1/4, 1/8, 1/4, 1/8,
		2.75/8, 2.75/8, 2.5/8,
		1/8, 1/8, 1/4, 1/8, 3/8,
		1/4, 1/8, 1/8, 1/8, 1/8, 1/4,
		1/8, 1/8, 1/4, 1/8, 1/4, 1/8,
		2.75/8, 2.75/8, 2.5/8, 1
	] * 1.15),
	\modFB, Pseq([
		0, 0, 0, 0.4, 0.6,
		0, 0, 0.4, 0.6, 0.4, 0,
		0, 0, 0, 0.4, 0.6, 0,
		0.6, 0.8, 1,
		0, 0, 0, 0.4, 0.6,
		0, 0, 0.4, 0.6, 0.4, 0,
		0, 0, 0, 0.4, 0.6, 0,
		0.6, 0.8, 1, 0.4
	]),
	\degree, Pseq([
		0, 0, 0, 7, 6,
		0, 0, 2, 3, 2, 0,
		0, 0, 0, 6, 7, 0,
		5, 2, 4,
		0, 0, 0, 7, 6,
		0, 0, 2, 3, 2, 0,
		0, 0, 0, 6, 7, 0,
		5, 2, 4, 0
	])
).play)


(SynthDef(\FMRhodes1, {
    arg
    // standard meanings
    out = 0, freq = 440, gate = 1, pan = 0, amp = 0.1, att = 0.001, rel = 1, lfoSpeed = 4.8, inputLevel = 0.2,
    // all of these range from 0 to 1
    modIndex = 0.2, mix = 0.2, lfoDepth = 0.1;

    var env1, env2, env3, env4;
    var osc1, osc2, osc3, osc4, snd;

    env1 = Env.perc(att, rel * 1.25, inputLevel, curve: \lin).kr;
    env2 = Env.perc(att, rel, inputLevel, curve: \lin).kr;
    env3 = Env.perc(att, rel * 1.5, inputLevel, curve: \lin).kr;
    env4 = Env.perc(att, rel * 1.5, inputLevel, curve: \lin).kr;

    osc4 = SinOsc.ar(freq) * 6.7341546494171 * modIndex * env4;
    osc3 = SinOsc.ar(freq * 2, osc4) * env3;
    osc2 = SinOsc.ar(freq * 30) * 0.683729941 * env2;
    osc1 = SinOsc.ar(freq * 2, osc2) * env1;
    snd = Mix((osc3 * (1 - mix)) + (osc1 * mix));
  	snd = snd * (SinOsc.ar(lfoSpeed).range((1 - lfoDepth), 1));

    snd = snd * Env.asr(0, 1, 0.1).kr(gate: gate, doneAction: 2);
    snd = Pan2.ar(snd, pan, amp);

    Out.ar(out, snd);
},
metadata: (
	credit: "Nathan Ho",
	category: \keyboards,
	tags: [\pitched, \piano, \fm]
)
).add;
)



(Pbindef(\FMRhodes1,
	\instrument, "FMRhodes1",
    \scale, Scale.mixolydian,
	\ctranspose, -10,
    \legato, Pseq([0.9, 0.5, 0.5, 0.9, 0.9, 0.9, 0.9, 0.7, 1, 0.9, 1, 0.6, 0.3], inf),
	\dur, Pseq([4/3, 1/3, 1/3, 1/7, 6/7, 5/6, 1/6, 1/2, 2/6, 1/6, Rest(1.4), 1, 1/2], inf) * 1/2,
    \degree, Pseq([
        [0, 2, 4], 2, 4, 7, 8, 7, 0, [1, 3, 6], 5, [1, 3, 6], \rest, [-1, 1, 3], [1, 3, 5],
        [0, 2, 4]
	], 1),
    \mix, 0.2,
    \modIndex, 0.2,
    \lfoSpeed, 0.5,
    \lfoDepth, 0.4,
    \inputLevel, Pgauss(0.8, 0.1, inf),
    \amp, 0.2,
	\strum, Pwhite(0, 0.02)
).play)






~fm7SynthNames = 32.collect{|algoNum| "fm7algo%".format(algoNum).asSymbol};

(
~fm7SynthNames.do{|synthName, algo|
	SynthDef(synthName, {|out=0, dur=0.01, sustain=0, freqScale=0.5, spread=0.25, pan=0, feedback=1.0, amp=0.5|
		var env = Env.perc.kr(gate:1, timeScale: dur * (1+sustain), doneAction: Done.freeSelf);
		var ctls =
		[
			// freq, phase, amp
			[freqScale * 300, pi.rand, 1],
			[freqScale * 2500, pi.rand, 1],
			[freqScale * SinOsc.ar(Rand(0.1,10.0)).exprange(3,100), 0, 1],
			[freqScale * LFNoise2.ar(10).exprange(1300,0.5), 0, 1],
			[freqScale * ExpRand(30,1500), pi.rand, 1],
			[freqScale * ExpRand(30,500), pi.rand, 1]
		];

		var sig = FM7.arAlgo(algo, ctls , feedback * 2.0);
		sig = Splay.ar(sig, spread: spread, center: pan);
		sig = sig * env * amp;

		Out.ar(out, sig);
	}).add;
};
)

(
Pbind(
	\instrument, Pshuf(~fm7SynthNames, inf).trace,
	\dur, Pwhite(0.01,0.125)*10,
	\sustain, Pwhite(0.0,1.0),
	\feedback, Pshuf(Array.rand(8, 0.25,1.0),inf),
	\freqScale, Pxrand(Array.rand(8, 0.25,4.0),inf),
	\amp, Pwhite(0.125,0.5),
	\spread, Pwhite(0.0,1.0),
	\pan, Pwhite(-1.0,1.0)
).play;
)