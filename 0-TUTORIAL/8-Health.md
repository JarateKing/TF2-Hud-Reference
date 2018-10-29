# Health

Hudplayerhealth.res is the file that controls your health on the hud. It's the most prominent example of a hud file that doesn't use hudlayout.res, and its parent panel is positioned and resized from within hudplayerhealth.res itself. It can be found in:
```
resource/ui/hudplayerhealth.res
```

To reposition it, changed the xpos/ypos/wide/tall of HudPlayerHealth like you would for anything in hudlayout:
```
	"HudPlayerHealth"
	{
		"ControlName"	"EditablePanel"
		"fieldName"		"HudPlayerHealth"
		"xpos"			"0"
		"ypos"			"r120"
		"zpos"			"2"
		"wide"			"250"
		"tall"			"120"
		"visible"		"1"
		"enabled"		"1"	
		"HealthBonusPosAdj"	"35"
		"HealthDeathWarning"	"0.49"
		"HealthDeathWarningColor"	"HUDDeathWarning"
	}
```
Everything is fairly standard and functions like anything you'd see in hudlayout, until you reach HealthBonusPosAdj, HealthDeathWarning, and HealthDeathWarningColor. These are extra controls for PlayerStatusHealthBonusImage:
```
	"PlayerStatusHealthBonusImage"
	{
		"ControlName"	"ImagePanel"
		"fieldName"		"PlayerStatusHealthBonusImage"
		"xpos"			"73"
		"ypos"			"33"
		"zpos"			"2"
		"wide"			"55"
		"tall"			"55"
		"visible"		"0"
		"enabled"		"1"
		"image"			"../hud/health_over_bg"
		"scaleImage"	"1"	
	}
```
This element automatically gets resized based on your overheal / damage taken. HealthBonusPosAdj determines how much larger it gets, with the value being the maximum resize. HeathDeathWarning is the percent where you're considered low health, and runs the HudHealthDyingPulse animation. HealthDeathWarningColor is the color that HealthBonusPosAdj automatically gets recolored to, when at low health (overhealed does not have any recoloring).