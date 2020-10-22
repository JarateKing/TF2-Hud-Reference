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

Fonts in linux need to be 0.8x the size of windows fonts to appear the same. By consequence fonts in windows need to be 1.25x the size of linux fonts, if you do most hud work on linux. In some huds this won't make much of a difference and can look fine with both, but in some huds it can break without properly sized fonts. You can check out software that can be used to resize fonts [here](/0-TUTORIAL/0-Tools.md). But, through testing, one HUD developer who primarily uses linux has found that some skinny fonts render in too heavy, appearing bolder than they should.

The easiest method to account for this difference is to create two variants, one for windows and one for linux, with a different filename but the same font name, as shown below.

Additionally, it has been found that many symbol fonts, such as the ones used for HUD crosshairs and Main Menu icons, will have character margins appear broken, and this must be fixed with creating alternate font files for linux.

Capping all of this off, the same developer who discovered the font weight issue also discovered that much of the font issues are not based on the linux distro you are using (i.e. Ubuntu or Arch), but the desktop environment that was initially installed when you installed linux as a whole. As of now, two desktop environments (DEs) have been found to not require fixed symbol fonts, and when a font is set at 0.8x size, and had the weight cut in half within the font instances inside `clientscheme.res`, will render most fonts near identically to windows. The two DEs in question are XFCE, a lightweight but more advanced DE, and KDE Plasma. Given that the most common linux distro, Ubuntu, ships with Unity DE, based on Gnome, your HUD should be built to work in a DE that does not render fonts correctly.
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
