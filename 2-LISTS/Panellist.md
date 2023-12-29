# Panel list

This is a list of most panel types and their parameters.


## Panel
The most basic panel, all other panels derive from this.
Parameter | Info
--------- | ----
fieldName | Renames the panel
xpos | Position of the panel in the X axis
ypos | Position of the panel in the Y axis
zpos | Render priority of the panel
wide | Size of the panel in the X axis
tall | Size of the panel in the Y axis
visible | Visibility of the panel
enabled | Changes the colour of labels and disables buttons
proportionalToParent | Position & size values relative to the parent size, instead of screen size
fgcolor_override | Foreground colour
bgcolor_override | Background colour
alpha | Opacity of the panel 0-255
paintbackground | Should the background be painted
PaintBackgroundType | How the background should be painted. Textures can be changed with Texture*</br>0 = Square corners</br>1 = Textured (Uses Texture1)</br>2 = Rounded corners</br>3 = Rounded Corners with horizontal fade
Texture1 | Top left
Texture2 | Top Right
Texture3 | Botttom Right
Texture4 | Bottom Left
RoundedCorners | Which corners are rounded
paintborder | Should the panel have a border
border | What border to use
pin_to_sibling | Pin the panel's position to another panel on the same level in the hierarchy
pin_corner_to_sibling | Which corner should be pinned to the sibling
pin_to_sibling_corner | To which corner of the sibling should the panel be pinned
mouseinputenabled | Should the panel listen for mouse inputs
keyboardinputenabled | Should the panel listen for keyboard inputs
tooltiptext | Text to display when hovering over the panel
actionsignallevel | Allows nested child buttons to add their distant parents as action signal targets
IgnoreScheme
usetitlesafe
ForceStereoRenderToFrameBuffer
tabPosition
autoResize
PinCorner
PinnedCornerOffSetX
PinnedCornerOffSetY
UnpinnedCornerOffSetX
UnpinnedCornerOffSetY
navUp
navDown
navLeft
navRight
navToRelay
navActivate
navBack


## EditablePanel
A panel that can have other panels inside of it. Derives from Panel.
Parameter | Info
--------- | ----
skip_autoresize | 


## Label
A panel with text. Derives from Panel.
Parameter | Info
--------- | ----
labelText | Text to display
font | What font to use
textAlignment | Where the text should align
textinsetx | Move text in X axis
textinsety | Move text in Y axis
use_proportional_insets | Insets are proportional to screen size
wrap | Should the text wrap when exceeding panel bounds
centerwrap | Same as above but centered
auto_wide_tocontents | The panel's wide value is automatically changed to fit the text
auto_tall_tocontents | The panel's tall value is automatically changed to fit the text
allcaps | Use only uppercase letters
disabledfgcolor2_override | Foreground colour when enabled == 0
dulltext | Should the text use dull colours
brighttext | Should the text use bright colours
associate


## Button
A panel that can fire a command when activated. Derives from Label.
Parameter | Info
--------- | ----
command | Command of the button
selected | Draws selected by default
stayselectedonclick | When clicked on, sets selected to 1
stay_armed_on_click | Don't revert back to default state when clicked
button_activation_type | How the button behaves</br>0 = When pressed sets depressed colours and activates command when released</br>1 = Activates command when pressed</br>2 = Activates command when released, doesn't set selected colours
sound_armed | Sound when hovered over
sound_depressed | Sound when pressing button
sound_released | Sound when releasing button
defaultFgColor_override | Foreground colour
defaultBgColor_override | Background colour
armedFgColor_override | Foreground colour when hovered
armedBgColor_override | Background colour when hovered
depressedFgColor_override | Foreground colour when clicked on
depressedBgColor_override | Background colour when clicked on
selectedFgColor_override | Foreground colour when selected
selectedBgColor_override | Background colour when selected
keyboardFocusColor_override
blinkFgColor_override
default


## ToggleButton
A button that can be toggled on and off. Derives from Button.


## CheckButton
A button that looks like a checkbox. Derives from ToggleButton.
Parameter | Info
--------- | ----
smallcheckimage | Use a smaller check image


## ExpandButton
A Button that looks like an arrow. Derives from ToggleButton.


## RichText
A panel with text that can scroll and can use a file for its contents. Derives from Panel.
Parameter | Info
--------- | ----
text | Text to display
textfile | A text file to display eg. "resource/text.txt"
scrollbar | Should the scrollbar be enabled
maxchars


## ImagePanel
A panel that displays an image. Derives from Panel.
Parameter | Info
--------- | ----
image | The image to display
fillcolor | Background colour
drawcolor | What colour to draw the image with
scaleImage | Whether to scale the image
scaleAmount | How much to scale the image, set to 0 for full size
tileImage | Repeat the image endlessly
tileHorizontally | Repeat the image endlessly in the X axis
tileVertically | Repeat the image endlessly in the Y axis
rotation | Rotate image 90 degrees
positionImage


## ScalableImagePanel
A panel that displays an image. Derives from Panel.
Parameter | Info
--------- | ----
image | The image to display
drawcolor | What colour to draw the image with
src_corner_width | How big the texture's corners are in the X axis
src_corner_height | How big the texture's corners are in the Y axis
draw_corner_width | How big to draw the corners in the X axis
draw_corner_height | How big to draw the corners in the Y axis


## CBitmapImagePanel
An image that can maintain its aspect ratio when resized. Derives from Panel.
Parameter | Info
--------- | ----
image | The image to display
imagecolor | What colour to draw the image with
imageAlignment | Where the image should align
preserveAspectRatio | Should the aspect ratio be maintained
filtered


## TextEntry
A panel you can type text in. Derives from Panel.
Parameter | Info
--------- | ----
font | What font to use
textHidden | Censor the text
editable | Allow the user to change the text
maxchars | Maximum amount of characters allowed
NumericInputOnly | Only allow numbers
selectallonfirstfocus
unicode


## ComboBox
A panel with a drop down list. Derives from TextEntry.
Parameter | Info
--------- | ----
border_override | Changes the border


## Slider
A panel with a movable slider. Derives from Panel.
Parameter | Info
--------- | ----
leftText | Text on the left
rightText | Text on the right
thumbwidth | Width of the slider
numTicks | Number of lines along the slider
rangeMin | What value the slider starts at
rangeMax | What value the slider ends at


## ProgressBar
A segmented progress bar. Derives from Panel.
Parameter | Info
--------- | ----
variable | What to measure
progress


## ContinuousProgressBar
Derives from ProgressBar.


## CircularProgressBar
Derives from ProgressBar
Parameter | Info
--------- | ----
fg_image | Image to use as the progress bar
bg_image | Image to use as the background



## RotatingProgressBar
Derives from ProgressBar
Parameter | Info
--------- | ----
image | Image that rotates
rotating_x | X position of the image
rotating_y | Y position of the image
rotating_wide | Wide of the image
rotating_tall | Tall of the image
start_degrees | Rotation of the image when variable == 0
end_degrees | Rotation of the image when variable == 100
rot_origin_x_percent | X position of what point the image rotates around, float value 0.0 - 1.0
rot_origin_Y_percent | Y position of what point the image rotates around, float value 0.0 - 1.0
approach_speed | The speed of rotation











