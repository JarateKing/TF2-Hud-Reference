# Ammo

Hudammoweapons.res controls the ammo used by weapons. It is only visible when using a weapon with ammo (not melee or mediguns, or example). It can be found in:
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

## Ammo BG Images

HudWeaponAmmoBG and HudWeaponLowAmmoImage are the backgrounds that appear behind the ammo, with HudWeaponAmmoBG being what normally appears and HudWeaponLowAmmoImage flashing when ammo is low.

```
	"HudWeaponAmmoBG"
	{
		"ControlName"	"CTFImagePanel"
		"fieldName"		"HudWeaponAmmoBG"
		"xpos"			"4"
		"ypos"			"0"
		"zpos"			"1"
		"wide"			"90"
		"tall"			"45"
		"visible"		"1"
		"enabled"		"1"
		"image"			"../hud/ammo_blue_bg"
		"scaleImage"	"1"	
		"teambg_2"		"../hud/ammo_red_bg"
		"teambg_3"		"../hud/ammo_blue_bg"	
	}
	"HudWeaponLowAmmoImage"
	{
		"ControlName"	"ImagePanel"
		"fieldName"		"HudWeaponLowAmmoImage"
		"xpos"			"4"
		"ypos"			"0"
		"zpos"			"0"
		"wide"			"90"
		"tall"			"45"
		"visible"		"0"
		"enabled"		"1"
		"image"			"../hud/ammo_red_bg"
		"scaleImage"	"1"	
		"teambg_2"		"../hud/ammo_red_bg"
		"teambg_3"		"../hud/ammo_blue_bg"	
	}
```

Notably they are of type CTFImagePanel, which is essentially an imagepanel that can change the image used depending on what team. The material specified with teambg_2 will be the red team, and teambg_3 will be the blu team, with "image" being the fallback in circumstances where the player isn't on either team.

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

It's worth noting that there isn't anything special about these labels, other than how they get automatically hidden. Fundamentally, the only thing different between AmmoInClip and AmmoInReserve (and also their shadow versions) are their default parameters. Because of this, it's possible (and done in some huds) to create new labels with "%Ammo%" that are visible regardless of which type of weapon you're using, and then make AmmoInClip and AmmoInClipShadow use "%AmmoInReserve%" or something else entirely, so that you can have more elaborate reserve ammo styles.

##
<table>
<tbody>
<tr>
<td><a href="/0-TUTORIAL/6-Hudlayout.md">Prev</a></td>
<td  width="50%"></td>
<td><a href="/README.md#readme">Home</a></td>
<td  width="50%"></td>
<td><a href="/0-TUTORIAL/8-Health.md">Next</a></td>
</tr>
</tbody>
</table>