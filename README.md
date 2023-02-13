<div align="center">
  <img src="https://github.com/gexahedron/domblar/blob/main/assets/domblar0.png?raw=true">
</div>

# Domblar

Algorithmic Music Composition Assistant, with a leaning towards (xen)tonality, in Python and SuperCollider.

# Music examples

Check out the [https://github.com/gexahedron/domblar/blob/main/assets/recordings/](https://github.com/gexahedron/domblar/blob/main/assets/recordings/) folder.

# Setup:

1. Install Dexed VST, version 0.9.7 (version 0.9.6 has problems with parameter automation) - [https://github.com/asb2m10/dexed/releases/tag/NIGHTLY](https://https://github.com/asb2m10/dexed/releases/tag/NIGHTLY)
   * (on MacOS) put .vst3 file to "/Library/Audio/Plug-ins/VST3" folder;
   * (on MacOS) because version 0.9.7 is unsigned, run in terminal `sudo xattr -rd com.apple.quarantine /Library/Audio/Plug-ins/VST3/Dexed.vst3` (which also requires sudo, unfortunately).
   * copy preset `assets/presets/dexed_preset.vstpreset` to `~/Library/Audio/presets/Digital Suburban/Dexed/` folder
2. Code is dependent on pyOSC3 library, to install it run `pip install pyOSC3` in terminal.

## Current restrictions/assumptions:

* The EDO code at the moment assumes octave equivalence
* code is tested in Python 3.8.10, on MacOS
