(thisProcess.nowExecutingPath.dirname+/+"melodyCreatorUtilities.scd").load;

(
var root, degree, octave;

var beatCreator = {
	while({
		~beatNtvls.size < 40 and:
		{ [\cadence, \cadenceRaised ].find([~beatNtvls[~beatNtvls.size - 1]]) === nil };
	}, {
		var fictaDegree = (~netDegrees + 1) % 7;
		~getNtvlOpts.value(~twoVoicesFifthAboveNtvls);
		if (
			~beatNtvls.size > 32 and:
			{ [1, 5].find([fictaDegree]) === nil },
			{
				~beatNtvls = ~beatNtvls.add(-1);
				if ([4,3,0].find([fictaDegree]) !== nil,
					{ ~beatNtvls = ~beatNtvls.add(\cadenceRaised) },
					{ ~beatNtvls = ~beatNtvls.add(\cadence) }
				);
			},
			{
				var chosenNtvl = ~ntvlOpts.choose;
				~beatNtvls = ~beatNtvls.add(chosenNtvl);
				~netDegrees = ~netDegrees + chosenNtvl;
				~netDegrees;
			}
		);
	});
};

var canonAndPause = {
	arg voices = 3;
	var beats, melody, createVoice, voice1, voice2, voice3, beginMass, canonAndPause, lastDegreeDict;
	~beatNtvls = [~twoVoicesFifthAboveNtvls.choose];
	root = 0;
	degree = (0..5).choose;
	octave = 4;
	~netDegrees = octave*7 + ~beatNtvls[0] + degree;
	beatCreator.value;
	melody = ~melodyCreator.value(~beatNtvls);
	lastDegreeDict = (
		1: degree,
		2: degree + 4
	);


	createVoice = {
		arg voiceNum = 1, totalVoices = 3;
		var stepData = Pseq(~melodyTailor.value(melody, voiceNum), 1);
		var pan = (voiceNum - 1)/(totalVoices - 1) - 0.5;
		Pmono(\simple,
			\stepData, stepData,
			\stepVelocity, Pkey(\stepData).collect({|e| e[0]}),
			\degree, Pfunc({|event| event[\stepVelocity] + lastDegreeDict[voiceNum] }),
			\dur, Pkey(\stepData).collect({|e| e[1]}),
			\scale, Scale.major,
			\octave, octave,
			\root, root,
			\pan, pan,
			\gate, 1,
			\amp, 1,
			\callback, { |event| lastDegreeDict[voiceNum] = event[\degree] }
		).play(quant: Quant(1, 0, voiceNum - 1));
	};
	voices.do({ |i| createVoice.value(i + 1) });
	((beats.size + 2) * (1/TempoClock.default.tempo)).yield;
};
Synth(\reverb);
Task({ { canonAndPause.value(2) }.loop; }).start;
)
