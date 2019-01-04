# Editing the Clientscheme

The clientscheme is the file that controls all named colors, borders, and fonts. It's split up into multiple sections.

To start with, there is the colors section. It contains all named colors (in RGBA format) used by the hud.
```
	Colors
	{
		// base colors
		"Orange"			"178 82 22 255"
		"OrangeDim"			"178 82 22 120"
		"LightOrange"		"188 112 0 128"
		"GoalOrange"		"255 133 0"
		"TFOrange"			"145 73 59 255"
		"Purple"			"137 69 99 255"
```

There is the BaseSettings section. This contains various settings for certain hud elements (mostly setting colors on certain windows). It can make use of the colors set in the above section, or it can just use the RGBA numbers, either works fine.
```
	BaseSettings
	{
		// vgui_controls color specifications
		ReplayBrowser.BgColor								"DarkBrown"
		ReplayBrowser.Details.TitleEdit.Carat.FgColor		"LightRed"
		ReplayBrowser.Button.ArmedBgColor					"TFOrange"
		ReplayBrowser.Button.DepressedBgColor				"TFOrange"
		ReplayBrowser.CollectionTitle.FgColor				"LightRed"
		ReplayBrowser.Warning.FgColor						"White"
		ReplayBrowser.ScrollBar.SliderButton.FgColor		"TransparentYellow"
		ReplayBrowser.Search.BgColor						"TanDark"
		ReplayBrowser.Search.FgColor						"White"
```

The bitmap fonts section is very finnicky and can mostly be ignored. It contains definitions for bitmap fonts, which are used for 360 controller and steam controller buttons.
```
	BitmapFontFiles
	{
		// UI buttons, custom font, (256x64)
		"Buttons"		"materials/vgui/fonts/buttons_32.vbf"
		"ButtonsSC"		"materials/vgui/fonts/buttons_sc.vbf"
	}
```

Fonts are probably the most important part of the clientscheme. The unique identifier ("ExampleFont") is what's used by hud elements. The "name" value specifies what font to use, based off the name in the font file declarations (which will be discussed later). The "tall" value is how big the font is (but depends on resolution). "antialias" being set to 1 says to smoothen the edges, if it were 0 the edges would be pixelized.
```
	Fonts
	{
		...
		"ExampleFont"
		{
			"1"
			{
				"name"		"TF2 Build"
				"tall"		"44"
				"antialias" "1"
			}
		}

		"ExampleFont2"
		{
			"1"
			{
				"name"		"TF2 Build"
				"tall"		"35"
				"antialias" "1"
			}
		}
		...
```

Borders are another section that needs to be defined in the clientscheme. There are several formats that can be used. This will be covered more in depth later.
```
	Borders
	{
		...
		ButtonBorder
		{
			"inset" "0 0 0 0"
			"backgroundtype" "2"
		}
		...
```

The CustomFontFiles section is needed to define what fonts the Fonts section can use. The "file" value should be the filepath of the ttf or otf file. The "name" value needs to be what the font is called (the easiest way to check is to rightclick the font and preview it, and check what "font name" says).
```
	CustomFontFiles
	{
		"1" "resource/tf.ttf"
		"2" "resource/tfd.ttf"
		"3"
		{
			"font" "resource/TF2.ttf"
			"name" "TF2"
		}
```

##
<table>
<tbody>
<tr>
<td><a href="/0-TUTORIAL/2-Editing-Elements.md">Prev</a></td>
<td  width="50%"></td>
<td><a href="/README.md#readme">Home</a></td>
<td  width="50%"></td>
<td><a href="/0-TUTORIAL/4-Editing-Animations.md">Next</a></td>
</tr>
</tbody>
</table>