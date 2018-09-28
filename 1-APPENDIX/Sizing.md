# Sizing

Sizing is fundamentally very similar to positioning.

## Regular Sizing

Setting wide and tall with just a number and no prefix will make that element be that number of units wide and tall.
```
	"wide" "50"
	"tall" "100"
```

## Fullscreen / Fill Sizing

Using the "f" prefix adds the number of horizontal screen units there are. The main usage of this is for "f0" which is the width of the screen, regardless of aspect ratio. For example, this will cover the entire screen:
```
	"wide" "f0"
	"tall" "480"
```

## Percent Sizing

Using the "p" prefix makes it use a percentage wide/tall of the screen. For example, this will be half as wide and half as tall as the screen for every aspect ratio:
```
	"wide" "p0.5"
	"tall" "p0.5"
```

## Other Percent Sizing

Using the "o" prefix is similar to the "p" prefix, except it uses the other direction. The primary use is to pair with a "p" value on the other axis, to avoid aspect ratio and keep things uniform. For example, this will be a perfect square:
```
	"wide" "o0.5"
	"tall" "p0.5"
```