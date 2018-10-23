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

## run-once cfgs

It is possible to make a config file only get executed once. This can be useful to set up some default settings for the hud, that the user may want to change later (for example, damage number color). To do so, valve.rc should include:
```
// manage the firstrun file
alias chud_firstrun "exec hud_firstrun"
exec hud_has_run.txt
chud_firstrun
```
Then the hud_firstrun.cfg file it references should contain:
```
// this cfg gets executed once ever, even after restarting tf2
// it can be re-exec'd by deleting cfg/hud_has_run.txt and restarting tf2

con_timestamp 0
con_logfile "cfg/hud_has_run.txt"
echo "alias chud_firstrun none"
con_logfile "console.txt"
con_timestamp 1
```
Any additional commands that the hud wants to include can be added to hud_firstrun.cfg.