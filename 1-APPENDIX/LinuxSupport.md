# Linux Support

Most parts of huds work fine in both windows and linux. There are a few exceptions that need to be accounted for, however.

## Filenames

Whereas files in windows do not care about using capital letters, linux is case sensitive and needs every file to be lowercase in order to be loaded. Whereas the following path name is valid in windows:
```
Resource/UI/MainMenuOverride.res
```
It needs to be like this in linux:
```
resource/ui/mainmenuoverride.res
```
If the file is capitalized and tries to be run with linux, it will fail to find the file and go with the default hud file instead.

## Fonts

Fonts in linux need to be 0.8x the size of windows fonts to appear the same. By consequence fonts in windows need to be 1.25x the size of linux fonts, if you do most hud work on linux. In some huds this won't make much of a difference and can look fine with both, but in some huds it can break without properly sized fonts. You can check out software that can be used to resize fonts [here](/0-TUTORIAL/0-Tools.md).

Two methods exist -- changing the sizes in clientscheme for each font definition, or creating a copy of the font file (in either `.ttf` or `.otf`) and resizing the glyphs themselves, saving with a different filename but same internal font name. As an example with the latter approach, we can have two font files:

```
jahud.otf
jahud_linux.otf
```

With this, the font file declaration in [clientscheme.res](/0-TUTORIAL/3-Editing-Clientscheme.md) can make use of the [$LINUX] and [$WINDOWS] tags to switch which file to use, depending on OS:
```
	"10"
	{
		"font" "resource/fonts/jahud.otf" [$WINDOWS]
		"font" "resource/fonts/jahud_linux.otf" [$LINUX]
		"name" "jahud"
	}
```

There are some other quirks with font rendering on linux, which can cause cropping or different weights. Namely, that depending on the desktop environment (DE) used, you may find fonts rendering slightly differently. XFCE and KDE Plasma render nearly identically to windows, as long as the font size is 0.8x and the weight is halved on skinny fonts. GNOME or Unity DE may have the cropping issues mentioned, and require additional fiddling with the font to fix.
