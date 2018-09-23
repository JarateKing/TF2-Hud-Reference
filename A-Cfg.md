# Cfg files

Some huds make use of config files.

## valve.rc

Valve.rc is a cfg file that gets automatically executed. It looks like this:
```
// load the base configuration
//exec default.cfg
r_decal_cullsize 1

// Setup custom controller
exec joystick.cfg

// run a user script file if present
exec autoexec.cfg

//
// stuff command line statements
//
stuffcmds

// display the startup level
startupmenu

sv_unlockedchapters 99
```

Because this file is usually not used by anything other than some huds, it's a good way to add in some custom cfg to exec.