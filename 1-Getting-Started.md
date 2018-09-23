# Getting Started

## custom folder

To begin with, every hud must have a folder in custom. This takes the form of:
```
steamapps\common\Team Fortress 2\tf\custom\HudName\
```
HudName can be any name of the hud. Inside of this hud will be various files and folders, taking the directory structure like so:
```
custom\HudName\info.vdf
custom\HudName\materials\
custom\HudName\resource\
custom\HudName\scripts\
```

## info.vdf

The info.vdf file is one used to specify what version of tf2 a hud is updated for, to protect against outdated huds causing crashes. As such, every hud needs to have an info.vdf file. It should contain:
```
"HudName"
{
    "ui_version"    "3"
}
```
As before, HudName can be whatever you want it to be, and its name doesn't matter. The "ui_version" value needs to be updated whenever a new update comes out. If the file does not exist, or "ui_version" is too low, the majority of hud files will not load.