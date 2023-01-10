( // init
s.options.sampleRate = 48000;
s.options.memSize = 8192 * 64; // increase this if you get "alloc failed" messages
s.options.maxNodes = 1024 * 32; // increase this if you are getting drop outs and the message "too many nodes"
s.options.numBuffers = 1024 * 16;
s.options.numOutputBusChannels = 2;
s.options.numInputBusChannels = 2;

s.latency = 0.1;

s.boot();

s.waitForBoot({
	("vst_utils.scd").loadRelative;
});
)


Server.killAll; // also callable from Python








//// some test code, not ready for production ////

// possible TODO: replace Pbinds with midi commands
// for more fine-grained sustain/duration control
c[0].midi.noteOn(3, 60, 100);
c[0].setn(0, [0.9]);
(
c[0].midi.noteOff(3, 60, 100);
c[0].midi.noteOn(3, 61, 100);
)
c[0].midi.noteOff(3, 60, 100);
c[0].midi.noteOff(3, 61, 100);

(
s.sendBundle(s.latency, c[0].midi.noteOn(0, 60, 100));
s.sendBundle(s.latency, c[0].midi.bend(0, 8092));
)


s.sendBundle(s.latency, c[0].midi.noteOff(0, 60, 100));

(
// using automatic bundling
s.bind {
	// c[0].midi.noteOn(0, 60, 100);
	c[0].midi.noteOff(0, 60, 100);
	// c[0].midi.noteOn(1, 64, 100);
	// c[0].midi.noteOn(2, 67, 100);
};
)