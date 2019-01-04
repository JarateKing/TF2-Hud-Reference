# Ubercharge

Hudmediccharge.res is the file that controls the medic's ubercharge meter, for both the regular charge meters and the vaccinator. It is located:
```
resource/ui/hudmediccharge.res
```

## Background Image

This is the background for the charge meter. It is very similar to the ammo background.

```
	"Background"
	{
		"ControlName"	"CTFImagePanel"
		"fieldName"		"Background"
		"xpos"			"0"
		"ypos"			"0"
		"zpos"			"0"
		"wide"			"130"
		"tall"			"65"
		"visible"		"1"
		"enabled"		"1"
		"image"			"../hud/medic_charge_blue_bg"
		"scaleImage"	"1"	
		"teambg_2"		"../hud/medic_charge_red_bg"
		"teambg_3"		"../hud/medic_charge_blue_bg"				
	}
```

## Label

The label itself is the percent number on the hud. This is a fairly standard label, but it utilizes localization for its labeltext. If the labeltext is set to "#TF_Ubercharge" it becomes "UBERCHARGE: 100%" and whereas "#TF_UberchargeMinHUD" it just becomes "100%".

IndividualChargesLabel is very similar, but is the charge count for the vaccinator. ChargeLabel will automatically get hidden when using the vaccinator, and IndividualChargesLabel will be shown.

```
	"ChargeLabel"
	{
		"ControlName"	"CExLabel"
		"fieldName"		"ChargeLabel"
		"xpos"			"30"
		"ypos"			"24"
		"zpos"			"2"
		"wide"			"90"
		"tall"			"15"
		"autoResize"	"1"
		"pinCorner"		"2"
		"visible"		"1"
		"enabled"		"1"
		"tabPosition"	"0"
		"labelText"		"#TF_Ubercharge"
		"labelText_minmode"		"#TF_UberchargeMinHUD"
		"textAlignment"	"west"
		"dulltext"		"0"
		"brighttext"	"0"
		"font"			"HudFontSmallest"
	}
	
	"IndividualChargesLabel"
	{
		"ControlName"	"CExLabel"
		"fieldName"		"IndividualChargesLabel"
		"xpos"			"30"
		"ypos"			"24"
		"zpos"			"2"
		"wide"			"90"
		"tall"			"15"
		"autoResize"	"1"
		"pinCorner"		"2"
		"visible"		"1"
		"enabled"		"1"
		"tabPosition"	"0"
		"labelText"		"#TF_IndividualUbercharges"
		"labelText_minmode"		"#TF_IndividualUberchargesMinHUD"
		"textAlignment"	"west"
		"dulltext"		"0"
		"brighttext"	"0"
		"font"			"HudFontSmallest"
	}
```

## Charge Bar

The charge bar is a element that fills itself gradually based off of your uber percent.

```
	"ChargeMeter"
	{	
		"ControlName"	"ContinuousProgressBar"
		"fieldName"		"ChargeMeter"
		"font"			"Default"
		"xpos"			"30"
		"ypos"			"38"
		"zpos"			"2"
		"wide"			"86"
		"tall"			"8"				
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"textAlignment"	"Left"
		"dulltext"		"0"
		"brighttext"	"0"
	}	
```

In addition, you can change colors by adding:
```
		"bgcolor_override" "0 0 0 0"
		"fgcolor_override" "255 255 255 255"
```

## Vaccinator Charge Bars

There are four different charge meters named ChargeMeter1, ChargeMeter2, ChargeMeter3, and ChargeMeter4 that are the charge bars for the vaccinator.

```
	"ChargeMeter1"
	{	
		"ControlName"	"ContinuousProgressBar"
		"fieldName"		"ChargeMeter1"
		"font"			"Default"
		"xpos"			"30"
		"ypos"			"38"
		"zpos"			"2"
		"wide"			"19"
		"tall"			"8"				
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"textAlignment"	"Left"
		"dulltext"		"0"
		"brighttext"	"0"
	}
```

## Health Cluster Icon

There are is also an image that goes with the bg panel.

```
	"HealthClusterIcon"
	{
		"ControlName"	"ImagePanel"
		"fieldName"		"HealthClusterIcon"
		"xpos"			"2"
		"ypos"			"17"
		"wide"			"36"
		"tall"			"36"
		"visible"		"1"
		"enabled"		"1"
		"image"			"../hud/ico_health_cluster"
		"scaleImage"	"1"	
	}
```

## Vaccinator Resist Icon

There is also an icon that shows what vaccinator setting you have. It automatically switches image based on which resistance you have.

```	
	"ResistIcon"
	{
		"ControlName"	"ImagePanel"
		"fieldName"		"ResistIcon"
		"xpos"			"0"
		"ypos"			"-25"
		"wide"			"36"
		"tall"			"36"
		"visible"		"1"
		"enabled"		"1"
		"image"			"../HUD/defense_buff_bullet_blue"
		"scaleImage"	"1"	
	}
```

##
<table>
<tbody>
<tr>
<td><a href="/0-TUTORIAL/8-Health.md">Prev</a></td>
<td  width="50%"></td>
<td><a href="/README.md#readme">Home</a></td>
<td  width="50%"></td>
<td><a href="/0-TUTORIAL/10-Damage-Numbers.md">Next</a></td>
</tr>
</tbody>
</table>