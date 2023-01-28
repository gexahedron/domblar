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


Server.killAll; // also callable from Python with "d = Domblar(...); d.stop_server()"
