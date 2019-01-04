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

## Health labels

The health value is a standard label. In fact there's nothing special about it, and you can put multiple different labels using %Health% as their labeltext as you want (which is common for giving the health label a shadow).
```
	"PlayerStatusHealthValue"
	{
		"ControlName"	"CExLabel"
		"fieldName"		"PlayerStatusHealthValue"
		"xpos"			"76"
		"ypos"			"52"
		"zpos"			"5"
		"wide"			"50"
		"tall"			"18"
		"visible"		"1"
		"enabled"		"1"
		"labelText"		"%Health%"
		"textAlignment"	"center"	
		"font"			"HudClassHealth"
		"fgcolor"		"TanDark"
	}
```
Many custom huds will use hud animations to make the health value change if you're overhealed / at low health. If you're making your hud do this or modifying another hud that does, you will have to change the HudHealthBonusPulse and HudHealthDyingPulse animations set the fgcolor to what you want, and have HudHealthBonusPulseStop and HudHealthDyingPulseStop set it back to the original color.

PlayerStatusMaxHealthValue is a bit different in that it only appears when you've taken damage. It's not out of the ordinary otherwise.
```
	"PlayerStatusMaxHealthValue"
	{
		"ControlName"	"CExLabel"
		"fieldName"		"PlayerStatusMaxHealthValue"
		"xpos"			"76"
		"ypos"			"20"
		"zpos"			"6"
		"wide"			"50"
		"tall"			"18"
		"visible"		"1"
		"enabled"		"1"
		"labelText"		"%MaxHealth%"
		"textAlignment"	"center"	
		"font"			"DefaultSmall"
		"fgcolor"		"TanDark"
	}
```

## Status images

The rest of the file is many different status effect images. They all follow the same general format:
```
	"PlayerStatusBleedImage"
	{
		"ControlName"	"ImagePanel"
		"fieldName"		"PlayerStatusBleedImage"
		"xpos"			"85"
		"ypos"			"0"
		"zpos"			"7"
		"wide"			"32"
		"tall"			"32"
		"visible"		"1"
		"enabled"		"1"
		"scaleImage"	"1"	
		"image"			"../vgui/bleed_drop"
		"fgcolor"		"TanDark"
	}
```
These don't appear by default, and only become visible when affected by the status effect.

Notably, these are hard to reposition, just changing xpos and ypos will not work. You can pin to corner for these to force their position however, as described in [here](/1-APPENDIX/Positioning.md#pin-to-corner).

##
<table>
<tbody>
<tr>
<td><a href="/0-TUTORIAL/7-Ammo.md">Prev</a></td>
<td  width="50%"></td>
<td><a href="/README.md#readme">Home</a></td>
<td  width="50%"></td>
<td><a href="/0-TUTORIAL/9-Ubercharge.md">Next</a></td>
</tr>
</tbody>
</table>