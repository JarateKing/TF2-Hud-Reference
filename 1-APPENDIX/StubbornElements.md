# Stubborn Elements

Some elements are very difficult to edit, and require some uncommon methods or workarounds to edit.

## Dashboard Dimmer

The dashboard dimmer is an element on the mainmenu that appears when you press the play button and open the play list. It's difficult to edit because it doesn't appear in any files, at first it doesn't seem to be overrideable in mainmenuoverride.res, and gets only gets loaded (from code) when either the play menu or the console is opened.

The solution is to add this to the mainmenuoverride.res:
```
	"DashboardDimmer"
	{
		"wide" "0"
		"tall" "0"
	}
```
And add this to valve.rc / your autoexec.cfg:
```
// remove dimmer
wait 5; showconsole; wait; incrementvar mat_antialias -100 100 1; hideconsole; wait 5; incrementvar mat_antialias -100 100 -1
```