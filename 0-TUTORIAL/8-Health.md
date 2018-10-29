# Health

Hudplayerhealth.res is the file that controls your health on the hud. It's the most prominent example of a hud file that doesn't use hudlayout.res, and its parent panel is positioned and resized from within hudplayerhealth.res itself. It can be found in:
```
resource/ui/hudplayerhealth.res
```

To reposition it, changed the xpos/ypos/wide/tall of HudPlayerHealth:
```
	"HudPlayerHealth"
	{
		"ControlName"	"EditablePanel"
		"fieldName"		"HudPlayerHealth"
		"xpos"			"0"		[$WIN32]
		"xpos_minmode"	"-5"		[$WIN32]
		"ypos"			"r120"	[$WIN32]
		"ypos_minmode"	"r88"	[$WIN32]
		"xpos"			"32"	[$X360]
		"ypos"			"r144"	[$X360]
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
