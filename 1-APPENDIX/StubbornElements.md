# Stubborn Elements

Some elements are very difficult to edit, and require some uncommon methods or workarounds to edit.

## Dashboard Dimmer

The dashboard dimmer is an element on the mainmenu that appears when you press the play button and open the play list. It dims out most of the screen (but leaves a bit at the bottom, which looks bad in most huds). It's difficult to edit because it doesn't appear in any files, at first it doesn't seem to be overrideable in mainmenuoverride.res, and only gets loaded (from code) when either the play menu or the console is opened.

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

The idea behind this is to:
1. open the console, which loads the dimmer element
2. change the mat_antialias value, which reloads the mainmenu
3. the reload checks mainmenuoverride.res and applies the wide and tall for dashboarddimmer to the now existing element, effectively hiding it
4. hide the console since it was only needed for loading the dimmer element
5. change the mat_antialias value back to what it was before