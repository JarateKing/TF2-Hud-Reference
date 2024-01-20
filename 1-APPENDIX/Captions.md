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

Captions themselves are defined in `closecaption_english.dat`. This is a compiled data file that can't be easily read or edited, and instead `closecaption_english.txt` contains the source human-readable and editable captions. This must then be compiled with the `captioncompiler.exe` utility found in a tf2 install's `bin` folder.

The format for `closecaption_english.txt` looks like:

```
"lang"
{ 
	"Language" "english" 
	"Tokens" 
	{
		"soundname" "text"
		"soundname2" "other text"
	}
}
```

There's various forms of formatting that can be included in caption text:

- `<B>`: bold text. If text is already bold, unboldens.
- `<I>`: italic text. If text is already italic, unitalizes.
- `<clr:255,255,255>`: text color in RGB format.
- `<cr>`: newline.
- `<sfx>`: marks caption as something to skip with `cc_subtitles 1`.
- `<delay:#>`: delays the caption for some number of seconds.
- `<len:#>`: shows the caption for some amount of time, to a maximum of `cc_linger_time`.
- `<norepeat:#>`: the delay until this caption can appear again.

## Advanced Usage

### New Captions

The console variable `cc_lang` can be used to set the caption file used. Normally, this is used for `cc_lang french` to use `closecaption_french.dat` instead of `closecaption_english.dat`, for example.

However, we may create new caption files and refer to them. If we had `closecaption_competitive.dat` and `closecaption_competitive.txt`, we may use `cc_lang competitive` to use these captions.

It's important to note that both a `.dat` and `.txt` file are needed to load captions. Despite this requirement, all caption data is loaded from `.dat` and by extensions `.txt` can be empty, like so:

```
"lang"
{ 
	"Language" "blank" 
	"Tokens" 
	{
		//blank
		//the .txt used to compile was not provided but is needed to load non-base .dat files into the game
	}
}
```

It can be used to refer to caption files in a subfolder as well: if we have a caption file like `resource/closecaption_/competitive.dat`, we can use `cc_lang /competitive` to use this. This can be used to better organize collections of caption files.

### Reloading Captions

If captions have been edited and recompiled while TF2 is running, we can reload captions by changing `cc_lang` to some other caption file and then changing `cc_lang` back to our desired caption file.

### Script Integration

The console command `cc_emit` can run arbitrary captions. With this, we can use captions as a way to show information from scripts. For example, if we had the captions:

```
"#slot1" "Switched to slot 1"
"#slot2" "Switched to slot 2"
"#slot3" "Switched to slot 3"
```

Then we can integrate this into a script:

```
bind 1 "slot1; cc_emit #slot1"
bind 2 "slot2; cc_emit #slot2"
bind 3 "slot3; cc_emit #slot3"
```

### Decompiling

Decompiling captions can be done with the [Source Caption Decompiler](https://github.com/JarateKing/sourcecaptiondecompiler) program.

## Further Reading:

Clovervidia's guides:

- https://steamcommunity.com/sharedfiles/filedetails/?id=167785751
- https://www.reddit.com/r/tf2scripthelp/wiki/captions/
