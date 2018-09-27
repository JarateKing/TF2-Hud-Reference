# Colors

Colors are very commonly used in huds.

## Color Format

All colors in tf2 follow the RGBA format (red green blue alpha) using decimal numbers between 0 and 255. For example, the following will set a label to be pure white and completely opaque:
```
	"fgcolor" "255 255 255 255"
```

## Example Colors

Name | Ex | Code
---- | -- | -----
Black | ![#000000](https://placehold.it/15/000000/000000?text=+) | 0, 0, 0, 255
White | ![#FFFFFF](https://placehold.it/15/ffffff/000000?text=+) | 255, 255, 255, 255
Gray | ![#7F7F7F](https://placehold.it/15/7f7f7f/000000?text=+) | 127, 127, 127, 255
Red | ![#FF0000](https://placehold.it/15/ff0000/000000?text=+) | 255, 0, 0, 255
Green | ![#00FF00](https://placehold.it/15/00ff00/000000?text=+) | 0, 255, 0, 255
Blue | ![#0000FF](https://placehold.it/15/0000ff/000000?text=+) | 0, 0, 255, 255
Yellow | ![#FFFF00](https://placehold.it/15/ffff00/000000?text=+) | 255, 0, 0, 255
Cyan | ![#00FFFF](https://placehold.it/15/00ffff/000000?text=+) | 0, 255, 255, 255
Magenta | ![#FF00FF](https://placehold.it/15/ff00ff/000000?text=+) | 255, 0, 255, 255

There are several good resources for mixing colors, such as:
* https://www.mathsisfun.com/hexadecimal-decimal-colors.html
* https://www.rapidtables.com/web/color/RGB_Color.html
* http://colorizer.org/

## Additive Colors

Fonts and some panels can use additive colors, by using the additive tag:
```
	"additive" "1"
```

Additive colors add their rgb values to whatever is below them. For example, if you had a panel with the color:
```
	"bgcolor" "255, 100, 0, 255"
```
And added a panel with additive colors above it with the color:
```
	"bgcolor" "0, 100, 200, 255"
```
The resulting color drawn to the screen will be:
```
	255+0, 100+100, 0+200, 255 = 255, 200, 200, 255
```

As a consequence, if an additive color is white, the resulting color will always be white. To lighten a color, you can add an additive with some gray as its color.