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