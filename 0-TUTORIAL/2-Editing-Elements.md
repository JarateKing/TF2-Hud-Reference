# Editing Elements

If you open up any ui file, you will be greeted with something that looks like this:
```
"Resource/UI/HudAmmoWeapons.res"
{
	"HudWeaponAmmoBG"
	{
		"ControlName"	"CTFImagePanel"
		"fieldName"		"HudWeaponAmmoBG"
		"xpos"			"4"
		"xpos_minmode"	"28"
		"ypos"			"0"
		"ypos_minmode"	"7"
		"zpos"			"1"
		"wide"			"90"
		"tall"			"45"
		"visible"		"1"
		"enabled"		"1"
		"image"			"../hud/ammo_blue_bg"
		"scaleImage"	"1"	
		"teambg_2"		"../hud/ammo_red_bg"
		"teambg_2_lodef"	"../hud/ammo_red_bg_lodef"
		"teambg_3"		"../hud/ammo_blue_bg"
		"teambg_3_lodef"	"../hud/ammo_blue_bg_lodef"			
	}
	"HudWeaponLowAmmoImage"
	{
		"ControlName"	"ImagePanel"
		"fieldName"		"HudWeaponLowAmmoImage"
		"xpos"			"4"
		"xpos_minmode"	"28"
		"ypos"			"0"
		"ypos_minmode"	"7"
		"zpos"			"0"
		"wide"			"90"
		"tall"			"45"
		"visible"		"0"
		"enabled"		"1"
		"image"			"../hud/ammo_red_bg"
		"scaleImage"	"1"	
		"teambg_2"		"../hud/ammo_red_bg"
		"teambg_2_lodef"	"../hud/ammo_red_bg_lodef"
		"teambg_3"		"../hud/ammo_blue_bg"
		"teambg_3_lodef"	"../hud/ammo_blue_bg_lodef"			
	}
	...
```

Let's dissect this a bit. To start off with, we have the file name, and an open curly bracket. For the most part, it can be ignored.
```
"Resource/UI/HudAmmoWeapons.res"
{
```

Then we have our first element. In this case, it's one uniquely identified by HudWeaponAmmoBG, and its named that too (each element's identifier and fieldname should be the same, and they should always be unique unless otherwise specified). And we also have the ControlName, which says what type of element this is. In this case it's a CTFImagePanel, which is an image panel that can be different depending on what team you're on.
```
	"HudWeaponAmmoBG"
	{
		"ControlName"	"CTFImagePanel"
		"fieldName"		"HudWeaponAmmoBG"
```

Then we get positioning and size values. "xpos" determines where the top-right of the element is horizontally. "ypos" is the same, but vertically instead. Any value on an element can have _minmode added to the end of it, which is the version to use when the minmode option is enabled (if there is no _minmode version of a value, it is the same in both). "zpos" determines which elements get drawn on top of eachother--if two elements would overlap, whichever has the higher zpos will be above the other. And wide and tall are how big the element is, horizontally and vertically respectively. You can readme more about positioning with xpos and ypos [here](/1-APPENDIX/Positioning.md).
```
		"xpos"			"4"
		"xpos_minmode"	"28"
		"ypos"			"0"
		"ypos_minmode"	"7"
		"zpos"			"1"
		"wide"			"90"
		"tall"			"45"
```

These two are very simple: can you see the element and is the element allowed to do what it needs to do. Unfortunately they're also pretty unreliable, and often that element will be forcefully enabled and visible from tf2's code and whatever you try to set these to doesn't matter (if you want to hide an element like this, you can set its xpos and ypos to 9999 and force it offscreen)
```
		"visible"		"1"
		"enabled"		"1"
```

These parts are specific to CTFImagePanel. "image" and the "teambg" values point to vmt files, to use as an image. "scaleimage" being set to 1 says that the image should be resized to match the "wide" and "tall" values exactly--if this was set to 0 or not set at all, the material would get drawn at its native size but get cut off / leave blank space depending on wide/tall values.
```
		"image"			"../hud/ammo_blue_bg"
		"scaleImage"	"1"	
		"teambg_2"		"../hud/ammo_red_bg"
		"teambg_2_lodef"	"../hud/ammo_red_bg_lodef"
		"teambg_3"		"../hud/ammo_blue_bg"
		"teambg_3_lodef"	"../hud/ammo_blue_bg_lodef"		
```

##
<table>
<tbody>
<tr>
<td><a href="/0-TUTORIAL/1-Getting-Started.md">Prev</a></td>
<td  width="50%"></td>
<td><a href="/README.md#readme">Home</a></td>
<td  width="50%"></td>
<td><a href="/0-TUTORIAL/3-Editing-Clientscheme.md">Next</a></td>
</tr>
</tbody>
</table>