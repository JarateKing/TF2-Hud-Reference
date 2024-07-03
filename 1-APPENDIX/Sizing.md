# Sizing

Sizing is fundamentally very similar to positioning. It makes use of the same units, which can be found [here](/1-APPENDIX/Positioning.md).

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

Using the "o" prefix makes it use a percentage wide/tall of the other axis. For example, this will be a perfect square:
```
	"wide" "o1.0"
	"tall" "p0.5"
```

## Proportional to Parent

Anything that uses f / p / o sizing (anything other than regular) can include the line:
```
	"proportionaltoparent" "1"
```
This will make them reference the size of their parent panel, rather than the screen dimensions. If they have no parent panel, they will continue to use the screen dimensions.
