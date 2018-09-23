# Materials

As you've seen before, some hud elements make use of materials. For example, in hudplayerhealth there is:
```
	"PlayerStatusHealthImageBG"
	{
		"ControlName"	"ImagePanel"
		"fieldName"		"PlayerStatusHealthImageBG"
		"xpos"			"73"
		"ypos"			"33"
		"zpos"			"3"
		"wide"			"55"
		"tall"			"55"
		"visible"		"1"
		"enabled"		"1"
		"image"			"../hud/health_bg"
		"scaleImage"	"1"	
	}	
```

The "image" value says where the file is located. By default it assumes that all materials will be in the vgui folder, and if they aren't then they have the "../" to work from the root materials folder.

If the vmt is missing, or the vtf that the vmt uses is missing, the source engine missing material will be displayed instead:
![Missing Material](/images/missing_material.png)

## Vmt File

The vmt file is what defines a material, and contains certain values and variables about how the texture should be drawn. Multiple different vmt's can point to the same texture file.

If we check out materials\hud\health_bg.vmt it looks like this:
```
"UnlitGeneric"
{
	"$translucent" 1
	"$baseTexture" "hud\health_bg"
	"$vertexcolor" 1
	"$no_fullbright" 1
	"$ignorez" 1
	"%keywords" "tf"
}
```

## Vtf File
The vtf file is how the file is actually drawn. Check out [the tools section](0-Tools.md#user-content-image-editors) for some information about how to edit these.
