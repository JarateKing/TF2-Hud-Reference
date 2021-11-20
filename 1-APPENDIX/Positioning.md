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
	"xpos" "c50"
	"ypos" "c100"
```
This element will be positioned 50 units from to the right of the center of the screen, and 100 units below the center of the screen. This value can be negative to go left / up from the center as well.

## Reverse Sized positioning

If they are set with a "rs" before the number, like so:
```
	"xpos" "rs1.0"
	"ypos" "rs1.0"
```
It is positioned like with the "r" prefix (from the bottom right corner, going in towards the top left) but by a percent of the element's size. In this case, it will be moved up exactly its height and moved left exactly its width, making it exist at the bottom right corner of the screen.

## Center Sized positioning

If they are set with a "cs" before the number, like so:
```
	"xpos" "cs-0.5"
	"ypos" "cs-0.5"
```
They will be positioned like the "c" prefix, but similar to "rs" is based off the size of the element. In this example, it will be half its width and height off from the center, effectively making the element's center be identical to the screen center.

## Pin to Corner

It is possible to automatically pin an element to another, effectively bypassing its xpos and ypos. This makes use of three values together:
```
	"pin_to_sibling" "HudElementAnchorName"
	"pin_corner_to_sibling" "PIN_TOPLEFT"
	"pin_to_sibling_corner" "PIN_TOPRIGHT"
```
This makes an element get positioned so that its top left corner is the same position as HudElementAnchorName's top right corner.

The valid corners to use are:
```
PIN_TOPLEFT
PIN_TOPRIGHT
PIN_BOTTOMLEFT
PIN_BOTTOMRIGHT
PIN_CENTER_TOP
PIN_CENTER_RIGHT
PIN_CENTER_BOTTOM
PIN_CENTER_LEFT
```

These are equivalent to using the following numbers instead:
```
0 -- 4 -- 1
|         |
7         5
|         |
2 -- 6 -- 3
```

Of note, this is often used to move elements that can't otherwise be moved. Some elements still can't be forcibly moved with this, but pinning elements will make most elements with hardcoded positions move.
