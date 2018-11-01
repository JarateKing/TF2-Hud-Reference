# Ammo

Hudammoweapons.res controls the ammo used by weapons. It can be found in:
```
resource/ui/hudammoweapons.res
```

## What is contained

Hudammoweapons.res contains the following elements:
```
"HudWeaponAmmoBG"
"HudWeaponLowAmmoImage"
"AmmoInClip"
"AmmoInClipShadow"
"AmmoInReserve"
"AmmoInReserveShadow"
"AmmoNoClip"
"AmmoNoClipShadow"
```

## Ammo Labels

AmmoInClip and AmmoInClipShadow are the ammo you currently have loaded when you have weapons that have clips (such as the scattergun), and are hardcoded to automatically get hidden when using weapons with no clip (such as the sniper rifle). Similarly, AmmoInReserve and AmmoInReserveShadow are the reserve (not in clip) ammo, and are also automatically hidden when using weapons with no clips. In contrast, AmmoNoClip and AmmoNoClipShadow are the ammo for weapons with no clip, and gets automatically hidden when using weapons with clips.

The six ammo labels are very similar. They all roughly follow the format:
```
	"AmmoInClip"
	{
		"ControlName"	"CExLabel"
		"fieldName"		"AmmoInClip"
		"font"			"HudFontGiantBold"
		"fgcolor"		"TanLight"
		"xpos"			"4"
		"ypos"			"0"
		"zpos"			"5"
		"wide"			"55"
		"tall"			"40"
		"visible"		"0"
		"enabled"		"1"
		"textAlignment"	"south-east"	
		"labelText"		"%Ammo%"
		
	}
```
The major difference being that AmmoInReserve and AmmoInReserveShadow use "%AmmoInReserve%" for their labeltext.