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
		"fieldName"				"CDamageAccountPanel"
		"text_x"				"0"
		"text_y"				"0"
		"delta_item_end_y"		"0"
		"PositiveColor"			"0 255 0 255"
		"NegativeColor"			"255 0 0 255"
		"delta_lifetime"		"1.5"
		"delta_item_font"		"HudFontSmall"
		"delta_item_font_big"	"HudFontMedium"
	}
```

## Hud Damage Numbers

It is possible for a hud to add damage numbers to the hud, that do not float or move. These involve labels that have the labeltext "%metal%", for example:
```
	"DamageAccountLabel"
	{
		"ControlName"		"CExLabel"
		"fieldName"		"DamageAccountLabel"
		"xpos"			"c-50"
		"ypos"			"c0"
		"zpos"			"100"
		"wide"			"100"
		"tall"			"50"
		"visible"		"1"
		"enabled"		"1"
		"labelText"		"%metal%"
		"textAlignment"		"center"
		"fgcolor"		"255 255 0 255"
		"font"			"HudFontMedium"
	}
```

Of note, the only setting that affects these damage numbers is whether or not damage numbers are enabled. They do not batch when using damage number batching, and the color settings do not change these labels' colors.