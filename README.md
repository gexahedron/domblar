<div align="center">
  <img src="https://github.com/gexahedron/domblar/blob/main/assets/domblar0.png?raw=true">
</div>

# Domblar

Algorithmic Music Composition Assistant, with a leaning towards (xen)tonality, in Python and SuperCollider.

# Music examples

Check out the [https://soundcloud.com/gexahedrop/sets/domblar-showcase](https://soundcloud.com/gexahedrop/sets/domblar-showcase) Soundcloud playlist.

# Setup:

1. Install Dexed VST, version 0.9.7 (version 0.9.6 has problems with parameter automation) - [https://github.com/asb2m10/dexed/releases/tag/NIGHTLY](https://https://github.com/asb2m10/dexed/releases/tag/NIGHTLY)
  * on MacOS
    * put .vst3 file to "/Library/Audio/Plug-ins/VST3" folder;
    * (on MacOS only) because version 0.9.7 is unsigned, run in terminal `sudo xattr -rd com.apple.quarantine /Library/Audio/Plug-Ins/VST3/Dexed.vst3` (which also requires sudo, unfortunately).
    * copy preset `assets/presets/dexed_preset.vstpreset` to `~/Library/Audio/presets/Digital\ Suburban/Dexed/` folder
  * on Linux:
    * put .vst3 file (actually, sometimes it is displayed as a folder) to "~/.vst3" folder (create folder if it doesn't exist);
    * copy preset `assets/presets/dexed_preset.vstpreset` to `~/.vst3/presets/Digital\ Suburban/Dexed/` folder (create folder if it doesn't exist)
  * install SuperCollider (on Linux I found the easiest to install Supercollider via ansible-tidalcycles)
  * install VSTPlugin for SuperCollider - get binaries here https://git.iem.at/pd/vstplugin/-/releases - and put the VSTPlugin folder to ~/.local/share/SuperCollider/Extensions/ - and then run "Recompile Class Library" from SuperCollider, Menu -> Language -> Recompile Class Library
2. Code is dependent on pyOSC3 library, to install it run `pip install pyOSC3` in terminal.

## Current restrictions/assumptions:

* The EDO code at the moment assumes octave equivalence
* code is tested in Python 3.8.10, on MacOS
