# Class Image

Hudplayerclass.res is the file that controls the class image. It is found at:
```
resource/ui/hudplayerclass.res
```

## Panel controls

Similar to health, the positioning of the panel is not controlled by hudlayout. It is the first element of hudplayerclass.res that controls it:
```
	"HudPlayerClass"
	{
		"ControlName"	"EditablePanel"
		"fieldName"		"HudPlayerClass"
		"xpos"			"0"
		"ypos"			"0"
		"zpos"			"1"
		"wide"			"f0"
		"tall"			"480"
		"visible"		"1"
		"enabled"		"1"		
	}
```

Generally, you don't have to edit this, since it covers the entire bounds of the screen. Most huds will instead just edit the positions of the elements themselves.

## Class Image

The class image itself is a fairly standard image panel (other than the ControlName). All else works as normal, except the image is set by code and cannot be manually changed.

```
	"PlayerStatusClassImage"
	{
		"ControlName"	"CTFClassImage"
		"fieldName"		"PlayerStatusClassImage"
		"xpos"			"25"
		"ypos"			"r88"
		"zpos"			"2"
		"wide"			"75"
		"tall"			"75"
		"visible"		"1"
		"enabled"		"1"
		"image"			"../hud/class_scoutred"
		"scaleImage"	"1"	
	}
```

## Spy Images

When disguised as a spy, other images are used in addition to the normal class image.

```
	"PlayerStatusSpyImage"
	{
		"ControlName"	"CTFImagePanel"
		"fieldName"		"PlayerStatusSpyImage"
		"xpos"			"3"
		"ypos"			"r67"
		"zpos"			"2"
		"wide"			"55"
		"wide_minmode"	"27"
		"tall"			"55"
		"tall_minmode"	"27"
		"visible"		"1"
		"enabled"		"1"
		"image"			"../hud/class_spyred"
		"scaleImage"	"1"	
		"teambg_2"		"../hud/class_spyred"
		"teambg_3"		"../hud/class_spyblue"			
	}	
	"PlayerStatusSpyOutlineImage"
	{
		"ControlName"	"CTFImagePanel"
		"fieldName"		"PlayerStatusSpyOutlineImage"
		"xpos"			"3"
		"ypos"			"r67"
		"zpos"			"7"
		"wide"			"55"
		"wide_minmode"	"27"
		"tall"			"55"
		"tall_minmode"	"27"
		"visible"		"0"
		"enabled"		"1"
		"image"			"../hud/class_spy_outline"
		"scaleImage"	"1"	
	}
```

If you wish to disable them or change how they're animated, you'll need to change the animations for them:
```
event HudSpyDisguiseChanged
{
	Animate PlayerStatusSpyOutlineImage		Alpha		"255"			Linear 0.0 0.2
	
	Animate PlayerStatusSpyOutlineImage		Position	"c-200 c-200"	Linear 0.0 0.2
	Animate PlayerStatusSpyOutlineImage		Size		"400 400"		Linear 0.0 0.2

	RunEvent HudSpyDisguiseHide	0.7
}

event HudSpyDisguiseHide
{
	Animate PlayerStatusSpyOutlineImage		Position	"3 413"			Linear 0.0 0.2
	Animate PlayerStatusSpyOutlineImage		Size		"55 55"			Linear 0.0 0.2
	
	Animate PlayerStatusSpyOutlineImage		Alpha		"0"				Linear 0.2 0.1
}

event HudSpyDisguiseFadeIn
{
	RunEvent HudSpyDisguiseChanged	0
	Animate PlayerStatusSpyImage			Alpha		"255"			Linear 0.9 0.1	
}

event HudSpyDisguiseFadeOut
{
	RunEvent HudSpyDisguiseChanged	0
	Animate PlayerStatusSpyImage			Alpha		"0"				Linear 0.9 0.1	
}
```

##
<table>
<tbody>
<tr>
<td><a href="/0-TUTORIAL/10-Damage-Numbers.md">Prev</a></td>
<td  width="50%"></td>
<td><a href="/README.md#readme">Home</a></td>
<td  width="50%"></td>
<td>Next</td>
</tr>
</tbody>
</table>