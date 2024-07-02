# Fonts
Parameter | Info
--------- | ----
name
weight
tall
scalex
scaley
yres | min & max Y resolution for this font
italic
underline
strikeout
symbol
antialias
dropshadow
outline
custom
bitmap
rotary
additive
blur
scanlines

# Borders
Parameter | Line Border | Image Border | Scalable Image Border | Info
--------- |:-----------:|:------------:|:---------------------:| ----
bordertype ||||"image" or "scalable_image"<br>If missing, uses the default line border.
inset | X ||| Order: left, top, right, bottom
backgroundtype | X | X | X
Left{} | X | | | Accepts "color" & "offset"
Top{} | X ||| -\|\|-
Right{} | X ||| -\|\|-
Bottom{} | X ||| -\|\|-
image | | X | X
paintfirst | | X | X | Whether or not to draw the border before the background & foreground or after.
tiled | | X
color ||| X
src_corner_height ||| X
src_corner_width ||| X
draw_corner_height ||| X
draw_corner_width ||| X


# ClientScheme

## statsummarry_embedded.res
Panel | Font | Color | Border
----- | ---- | ----- | ------
ClassCombo | ScoreBoardSmall
BarChartComboA<br>BarChartComboB | ScoreboardVerySmall

## mvmcriteria.res
Panel | Font | Color | Border
----- | ---- | ----- | ------
TourList | HudFontSmallest<br>HudFontSmall

# SourceScheme

## GameConsole
Panel | Font | Color | Border
----- | ---- | ----- | ------
ConsoleEntry | | | DepressedButtonBorder
ConsoleHistory | ConsoleText | Console.TextColor<br>Console.DevTextColor | DepressedButtonBorder
CompletionList | DefaultSmall | | 
