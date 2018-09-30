# Linux Support

Most parts of huds work fine in both windows and linux. There are a few exceptions that need to be accounted for, however.

## Filenames

Whereas files in windows can use capitals, linux is case sensitive and needs every file to be lowercase. Whereas the following path name is valid in windows:
```
Resource/UI/MainMenuOverride.res
```
It needs to be like this in linux:
```
resource/ui/mainmenuoverride.res
```

## Fonts

Fonts in linux need to be 0.8x the size of windows fonts. By consequence fonts in windows need to be 1.25x the size of linux fonts. You can check out software that can be used to resize fonts [here](/0-TUTORIAL/0-Tools.md).

The easiest method to account for this difference is to create two variants, one for windows and one for linux, with a different filename but the same font name.
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