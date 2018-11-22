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

