# Positioning

Positioning elements with xpos and ypos is simple in concept, but can be a bit more complicated than that.

## Screen size

It's important to mention that the units used for xpos and ypos are resolution dependent. On 640x480, it lines up with the pixels on the screen exactly. Any other resolution is not as accurate.

Resolution | horizontal units | vertical units
---------- | ---------------- | --------------
5:4 | 600 | 480
4:3 | 640 | 480
16:10 | 768 | 480
16:9 | ~853 | 480
1.85:1 | 888 | 480

## Standard positioning

If xpos and ypos are set with just a number and nothing else, like so:
```
	"xpos" "50"
	"ypos" "100"
```
This element will be positioned 50 units from the left, and 100 units down from the top. If this value is negative, it will be pushed off the screen, but may still be visible (if it is wide and tall enough).

## Reverse positioning

If they are set with an "r" before the number, like so:
```
	"xpos" "r50"
	"ypos" "r100"
```
This element will be positioned 50 units from the right, and 100 units up from the bottom. If this value is 0 or negative, the element will be pushed off the screen.

## Center positioning

If they are set with an "c" before the number, like so:
```
	"xpos" "r50"
	"ypos" "r100"
```
This element will be positioned 50 units from to the right of the center of the screen, and 100 units below the center of the screen. This value can be negative to go left / up from the center as well.