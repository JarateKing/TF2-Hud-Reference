# Hudlayout.res

Hudlayout.res controls the positioning and size of most panels (with some notable exceptions, such as health), and can be used for hud elements that are always visible ingame (notably, hud crosshairs or transparent viewmodels). It is found in the folder:
```
scripts/hudlayout.res
```

## Controlling Panels

Panels controlled by hudlayout (which is the majority of ones visible ingame) can be repositioned and resized. For example, one of the first panels inside hudlayout.res controls the ammo panel:
```
	HudWeaponAmmo
	{
		"fieldName" "HudWeaponAmmo"
		"visible" "1"
		"enabled" "1"
		"xpos"	"r95"	[$WIN32]
		"xpos_minmode"	"r85"	[$WIN32]
		"ypos"	"r55"	[$WIN32]
		"ypos_minmode"	"r36"	[$WIN32]
		"xpos"	"r131"	[$X360]
		"ypos"	"r77"	[$X360]
		"wide"	"94"
		"tall"	"45"
	}
```
If we cut out the excess, it becomes a bit more simple:
```
	HudWeaponAmmo
	{
		"fieldName" "HudWeaponAmmo"
		"visible" "1"
		"enabled" "1"
		"xpos"	"r95"
		"ypos"	"r55"
		"wide"	"94"
		"tall"	"45"
	}
```
Changing the xpos and ypos will move the ammo panel, which effectively moves everything contained in the hudammoweapons.res file.

A bit less intuitively, changing the wide and tall values will change the max size of the ammo panel. If something inside hudammoweapons.res is larger, or appears outside of that max size, it will be cut off and not visible. For this reason, some huds will choose to make their hudammoweapons.res control all positioning, and have their ammo panel in hudlayout cover the entire screen (doing this without adjusting hudammoweapons.res will result in your ammo being in the top right corner):
```
	HudWeaponAmmo
	{
		"fieldName" "HudWeaponAmmo"
		"visible" "1"
		"enabled" "1"
		"xpos"	"0"
		"ypos"	"0"
		"wide"	"f0"
		"tall"	"480"
	}
```