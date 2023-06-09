# Captions

Captions are short messages that play when certain sounds happen ingame.

There are a few parts involved in captions. Captions are enabled with a console command:

```
closecaption 1
```

And then can be further customized with other commands:

```
cc_subtitles 0 // if set to 1, don't show sfx-marked captions
cc_lang english // which caption file to use
cc_linger_time 1.0 // how long captions should be visible for
cc_predisplay_time 0.25 // how long to wait before showing a caption
cc_sentencecaptionnorepeat 4 // how long for a caption to not repeat
```

They can be stylized by adding to `hudlayout.res`:

```
	HudCloseCaption
	{
		"fieldName" "HudCloseCaption"
		"visible"	"1"
		"enabled"	"1"
		"xpos"		"c-250"
		"ypos"		"276"
		"wide"		"500"
		"tall"		"136"

		"BgAlpha"	"128"

		"GrowTime"		"0.25"
		"ItemHiddenTime"	"0.2"  // Nearly same as grow time so that the item doesn't start to show until growth is finished
		"ItemFadeInTime"	"0.15"	// Once ItemHiddenTime is finished, takes this much longer to fade in
		"ItemFadeOutTime"	"0.3"
		"topoffset"		"0"
	}
```

As well, in `clientscheme.res` there are various fonts that are used by captions: `CloseCaption_Normal`, `CloseCaption_Italic`, `CloseCaption_Bold`, `CloseCaption_BoldItalic`, and `CloseCaption_Small` that form the different types of fonts that a caption may use.
