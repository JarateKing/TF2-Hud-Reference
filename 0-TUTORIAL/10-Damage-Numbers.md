# Damage Numbers

Huddamageaccount.res is the file that controls the damage numbers that appear when you damage players. It is located:
```
resource/ui/huddamageaccount.res
```

## Damage Account

The default file only includes one element, the damage account panel, which controls floating damage numbers:
```
	"CDamageAccountPanel"
	{
		"fieldName"             "CDamageAccountPanel"
		"text_x"                "0"
		"text_y"                "0"
		"delta_item_end_y"      "0"
		"PositiveColor"         "0 255 0 255"
		"NegativeColor"         "255 0 0 255"
		"delta_lifetime"        "1.5"
		"delta_item_font"       "HudFontSmall"
		"delta_item_font_big"   "HudFontMedium"
	}
```

To explain what each does:
* text_y & text_y: offsets for damage numbers
* delta_item_end_y: how much the damage number will float up by
* delta_lifetime: how long the damage numbers will exist for
* delta_item_font: the regular font used
* delta_item_font_big: the font used when doing a crit
* PositiveColor: the color for healing someone
* NegativeColor: obsolete and useless, replaced with cvars

There are also some other settings that can be used, that are not included in the default hud:
```
		"EventColor"            "255 255 255 255" // med drops
		"RedRobotScoreColor"    "255 255 255 255" // robot destruction
		"BlueRobotScoreColor"   "255 255 255 255" // robot destruction
```

## Hud Damage Numbers

It is possible for a hud to add damage numbers to the hud, that do not float or move. These involve labels that have the labeltext "%metal%", for example:
```
	"DamageAccountLabel"
	{
		"ControlName"       "CExLabel"
		"fieldName"         "DamageAccountLabel"
		"xpos"              "c-50"
		"ypos"              "c0"
		"zpos"              "100"
		"wide"              "100"
		"tall"              "50"
		"visible"           "1"
		"enabled"           "1"
		"labelText"         "%metal%"
		"textAlignment"     "center"
		"fgcolor"           "255 255 0 255"
		"font"              "HudFontMedium"
	}
```

Of note, the only setting that affects these damage numbers is whether or not damage numbers are enabled. They do not batch when using damage number batching, and the color settings do not change these labels' colors.

##
<table>
<tbody>
<tr>
<td><a href="/0-TUTORIAL/9-Ubercharge.md">Prev</a></td>
<td  width="50%"></td>
<td><a href="/README.md#readme">Home</a></td>
<td  width="50%"></td>
<td><a href="/0-TUTORIAL/11-Class-Image.md">Next</a></td>
</tr>
</tbody>
</table>