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

// TODO: create a separate function
// Server.killAll;

// TODO: create a separate function
(
~synth_count = 3;
a = Array.fill(~synth_count , nil); // synths
c = Array.fill(~synth_count , nil); // controllers

~synth_count.do { arg i;
	a[i] = Synth(\vst_plugin);
	c[i] = VSTPluginController(a[i]);
	c[i].open("Dexed.vst3");
};
)

// TODO: create a separate function
// reset MPE and Mono mode for Dexed
(
3.do { arg i;
	c[i].loadPreset("dexed_preset");
};
)

// TODO: create a separate function
c[0].editor;

// TODO: create a separate function
c[0].getn(0, -1, action: {arg v; Post << v});

// TODO: create a separate function
// reset MPE and Mono mode for Dexed
c[0].savePreset("dexed_instrument");
c[0].loadPreset("dexed_instrument");




// maybe TODO: replace Pbinds with midi commands
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