# Panel list

This is a list of panel types and their parameters.


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
enabled | Changes the colour of labels and disables interaction with buttons, sliders, text boxes etc.
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

Default scheme values
Font | Color | Border
---- | ----  | ------
  | Panel.FgColor
  | Panel.BgColor 


## EditablePanel
A panel that can have other panels inside of it. Derives from Panel.
Parameter | Info
--------- | ----
skip_autoresize | 
eatmouseinput
showtooltipswhenmousedisabled


## Frame
Derives from EditablePanel.
Parameter | Info
--------- | ----
setclosebuttonvisible
settitlebarvisible
title
title_font
clientinsetx_override
titletextinsetX
titletextinsetY
infocus_bgcolor_override
outoffocus_bgcolor_override
titlebarbgcolor_override
titlebardisabledbgcolor_override
titlebarfgcolor_override
titlebardisabledfgcolor_override
frame_topGrip{} | ControlName: GripPanel
frame_bottomGrip{} | ControlName: GripPanel
frame_leftGrip{} | ControlName: GripPanel
frame_rightGrip{} | ControlName: GripPanel
frame_tlGrip{} | ControlName: GripPanel
frame_trGrip{} | ControlName: GripPanel
frame_blGrip{} | ControlName: GripPanel
frame_brGrip{} | ControlName: GripPanel
frame_caption{} | ControlName: CaptionGripPanel
frame_minimize{} | ControlName: FrameButton
frame_maximize{} | ControlName: FrameButton
frame_mintosystray{} | ControlName: FrameButton
frame_close{} | ControlName: FrameButton
frame_menu{} | ControlName: FrameSystemButton

Default scheme values
Font | Color | Border | Other
---- | ----  | ------ | -----
FrameTitleBar.SmallFont | FrameTitleBar.TextColor | FrameBorder | Frame.TransitionEffectTime
FrameTitleBar.Font | FrameTitleBar.BgColor | | Frame.FocusTransitionEffectTime
 MarlettSmall | FrameTitleBar.DisabledTextColor | | Frame.ClientInsetX
 Marlett | FrameTitleBar.DisabledBgColor | | Frame.ClientInsetY
   | Frame.BgColor | | Frame.TitleTextInsetX
   | Frame.OutOfFocusBgColor


## GripPanel
Derives from Panel.

Default scheme values
Font | Color | Border | Other
---- | ----  | ------ | -----
MarlettSmall | FrameGrip.Color1 |   | Frame.AutoSnapRange
Marlett | FrameGrip.Color2
   | FrameTitleBar.DisabledTextColor
   | FrameTitleBar.DisabledBgColor


## FrameButton
Derives from Button.

Default scheme values
Font | Color | Border | Other
---- | ----  | ------ | -----
   | FrameTitleButton.FgColor | TitleButtonBorder
   | FrameTitleButton.BgColor | TitleButtonDepressedBorder
   | FrameTitleButton.DisabledFgColor | TitleButtonDisabledBorder
   | FrameTitleButton.DisabledBgColor


## FrameSystemButton
Derives from MenuButton.

Default scheme values
Font | Color | Border | Other
---- | ----  | ------ | -----
   | FrameSystemButton.FgColor |  | FrameSystemButton.Icon
   | FrameSystemButton.BgColor | | FrameSystemButton.DisabledIcon


## PropertySheet
Derives from EditablePanel.
Parameter | Info
--------- | ----
tabxindent
tabxdelta
tabxfittotext
tabheight
tabheight_small
tabwidth
transition_time
tabskv{} | Controlname: PageTab

Default scheme values
Font | Color | Border | Other
---- | ----  | ------ | -----
DefaultVerySmall |  | PropertySheetBorder | PropertySheet.TransitionEffectTime
Default |


## PageTab
Derives from Button.
Parameter | Info
--------- | ----
selectedcolor
unselectedcolor
activeborder_override
normalborder_override

Default scheme values
Font | Color | Border | Other
---- | ----  | ------ | -----
DefaultVerySmall | PropertySheet.SelectedTextColor | TabActiveBorder | PropertySheet.TransitionEffectTime
Default | PropertySheet.TextColor | TabBorder


## ScrollableEditablePanel
Derives from EditablePanel.
Parameter | Info
--------- | ----
ScrollBar{} | ControlName: ScrollBar


## CExScrollingEditablePanel
A panel that can have other panels inside of it and can be scrolled. Derives from EditablePanel.
Parameter | Info
--------- | ----
allow_mouse_wheel_to_scroll | Only allow scrolling by dragging the slider
scroll_step | How much the scroll wheel scrolls
bottom_buffer | How much space to leave at the bottom
restrict_width | Make the contents fit inside the panel
ScrollBar{} | ControlName: CExScrollBar


## CScrollableList
Derives from CExScrollingEditablePanel


## CExpandablePanel
Derives from EditablePanel.
Parameter | Info
--------- | ----
resize_time | How quickly to resize panel
collapsed_height | How tall when collapsed
expanded_height | How tall when expanded


## ListPanel
Derives from Panel.
Parameter | Info
--------- | ----

Default scheme values
Font | Color | Border
---- | ----  | ------
Default | ListPanel.BgColor | ButtonDepressedBorder
  | ListPanel.TextColor
   | ListPanel.DisabledTextColor
   | ListPanel.SelectedTextColor
   | ListPanel.DisabledSelectedTextColor
   | ListPanel.EmptyListInfoTextColor


## SectionedListPanel
Derives from Panel.
Parameter | Info
--------- | ----
show_columns
linespacing
sectiongap
linegap

Default scheme values
Font | Color | Border
---- | ----  | ------
DefaultVerySmall | SectionedListPanel.HeaderTextColor | ButtonDepressedBorder
SectionedListPanel.Font | SectionedListPanel.DividerColor
   | SectionedListPanelHeader.BgColor
   | SectionedListPanel.BrightTextColor
   | SectionedListPanel.SelectedTextColor
   | SectionedListPanel.OutOfFocusSelectedTextColor
   | SectionedListPanel.SelectedBgColor
   | SectionedListPanel.TextColor
   | SectionedListPanel.BgColor
   | SectionedListPanel.OutOfFocusSelectedBgColor


## PanelListPanel
Derives from EditablePanel.
Parameter | Info
--------- | ----
autohide_scrollbar

Default scheme values
Font | Color | Border
---- | ----  | ------
  | ListPanel.BgColor | ButtonDepressedBorder

## CBaseASyncPanel
Derives from EditablePanel.
Parameter | Info
--------- | ----
refresh_delay | Float
asynchandling | "content" or "loading", not actually on the panel but rather on the panel's child


## CTFLeaderboardPanel
Derives from CBaseASyncPanel.
Parameter | Info
--------- | ----
entry_step
EvenTextColor
OddTextColor
LocalPlayerTextColor
ScoresContainer{} | ControlName: EditablePanel


## CLadderLobbyLeaderboard
Derives from CTFLeaderboardPanel.
Parameter | Info
--------- | ----


## Menu
Derives from Panel.

Default scheme values
Font | Color | Border
---- | ----  | ------
  | Menu.TextColor | MenuBorder
  | Menu.BgColor | 
  | BorderDark | 


## MenuSeperator
Derives from Panel.

Default scheme values
Font | Color | Border
---- | ----  | ------
  | Menu.SeparatorColor | 
  | Menu.BgColor | 




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

Default scheme values
Font | Color | Border
---- | ----  | ------
Default | Label.DisabledFgColor1
   | Label.DisabledFgColor2
   | Label.BgColor
   | Label.TextDullColor
   | Label.TextBrightColor
   | Label.TextColor
   | Label.SelectedTextColor


## CExLabel
An expanded label. Derives from Label.
Parameter | Info
--------- | ----
fgcolor | Foreground colour


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

Default scheme values
Font | Color | Border
---- | ----  | ------
   | Button.TextColor | ButtonBorder
   | Button.BgColor | ButtonDepressedBorder
   | Button.ArmedTextColor | ButtonKeyFocusBorder
   | Button.ArmedBgColor
   | Button.SelectedTextColor
   | Button.SelectedBgColor
   | Button.DepressedTextColor
   | Button.DepressedBgColor
   | Button.FocusBorderColor
   | Button.BlinkColor


## CExButton
Expanded button. Derives from Button.
Parameter | Info
--------- | ----
fgcolor | Foreground colour
border_default | Default border
border_armed | Border when hovered
border_disabled | Border when enabled == 0
border_selected | Border when selected == 1


## CExImageButton
A button that displays an image. Derives from CExButton.
Parameter | Info
--------- | ----
image_drawcolor | What colour to draw the image by default
image_armedcolor | What colour to draw the image when hovered
image_depressedcolor | What colour to draw the image when pressed
image_disabledcolor | What colour to draw the image when enabled == 0
image_selectedcolor | What colour to draw the image when selected == 1
image_default | What image to use by default
image_armed | What image to use when hovered
image_selected | What image to use when selected == 1
SubImage{} | ControlName: ImagePanel


## CImageButton
A button that displays an image. Derives from Button.
Parameter | Info
--------- | ----
scaleImage | Whether to scale the image
inactiveimage | Image to use by default
activeimage | Image to use when hovered
inactivedrawcolor | What colour to draw the image by default
activedrawcolor | What colour to draw the image when hovered

Default scheme values
Font | Color | Border
---- | ----  | ------
   | Button.TextColor | NoBorder
   | Button.ArmedTextColor
   | Button.DepressedTextColor


## ToggleButton
A button that can be toggled on and off. Derives from Button.

Default scheme values
Font | Color | Border
---- | ----  | ------
   | ToggleButton.SelectedTextColor |


## CheckButton
A button that looks like a checkbox. Derives from ToggleButton.
Parameter | Info
--------- | ----
smallcheckimage | Use a smaller check image

Default scheme values
Font | Color | Border
---- | ----  | ------
 MarlettSmall | CheckButton.TextColor | ButtonBorder
 Marlett | CheckButton.BgColor | ButtonDepressedBorder
   | CheckButton.Border1 | ButtonKeyFocusBorder
   | CheckButton.Border2
   | CheckButton.Check
   | CheckButton.SelectedTextColor
   | CheckButton.DisabledFgColor
   | CheckButton.DisabledBgColor
   | CheckButton.ArmedBgColor
   | CheckButton.DepressedBgColor
   | CheckButton.HighlightFgColor


## CvarToggleCheckButton
A checkbutton that displays the value of a cvar. Derives from CheckButton.
Parameter | Info
--------- | ----
cvar_name |
cvar_value |


## CExCheckButton 
Derives from CheckButton.


## ExpandButton
A button that looks like an arrow. Derives from ToggleButton.

Default scheme values
Font | Color | Border
---- | ----  | ------
 Marlett | ExpandButton.Color


## CTFTeamButton
A button that animates a model. Animation events are called idle_enabled, idle_disabled, enter_enabled, enter_disabled, exit_enabled, exit_disabled & hover_disabled. Only works in the team select menu. Derives from CExButton.
Parameter | Info
--------- | ----
associated_model | What model to animate
team
hover | Delay before animation


## CAutoFittingLabel
A label that changes the font to fit in the boundaries of the panel. Derives from Label.
Parameter | Info
--------- | ----
fonts{}
```
"fonts"
{
  "1"
  {
    "font"  "large_font"
  }
  "2"
  {
    "font"  "medium_font"
  }
  "3"
  {
    "font"  "small_font"
  }
}
```


## URLLabel
A button that opens a web page. Derives from Label.
Parameter | Info
--------- | ----
URLText | URL to the web page

Default scheme values
Font | Color | Border
---- | ----  | ------
 DefaultUnderline 


## RichText
A panel with text that can scroll and can use a text file for its contents. Derives from Panel.
Parameter | Info
--------- | ----
text | Text to display
textfile | A text file to display eg. "resource/text.txt"
scrollbar | Should the scrollbar be enabled
maxchars
ScrollBar{} | ControlName: ScrollBar

Default scheme values
Font | Color | Border | Other
---- | ----  | ------ | -----
 Default | RichText.TextColor |   | RichText.InsetX
 DefaultUnderline | RichText.BgColor | 
   | RichText.SelectedTextColor | 
   | RichText.SelectedBgColor | 


## CExRichText
An expanded rich text. Derives from RichText.
Parameter | Info
--------- | ----
font | What font to use
fgcolor | Foreground colour
image_up_arrow | Image for the scrollbar's up arrow
image_down_arrow | Image for the scrollbar's down arrow
image_line | Image for the scrollbar slider's background 
image_box | Image for the scrollbar slider
image_up_arrow_mouseover | Image for the scrollbar's up arrow when hovered
image_down_arrow_mouseover | Image for the scrollbar's down arrow when hovered
Line{} | ControlName: ImagePanel
Box{} | ControlName: ImagePanel
UpArrow{} | ControlName: CExImageButton
DownArrow{} | ControlName: CExImageButton
ScrollBar{} | ControlName: ScrollBar

Default scheme values
Font | Color | Border
---- | ----  | ------
   | Blank | NoBorder


## CRichTextWithScrollbarBorders
Same as above but uses borders instead of images for image_line & image_box. "Line" & "Box" are Panels instead of ImagePanels. Derives from CExRichText.


## CEconItemDetailsRichText
"Rich text control that knows how to fill itself with information that describes a specific item definition."
Parameter | Info
--------- | ----
highlight_color
itemset_color
link_color


## ScrollBar
A scrollbar. Derives from Panel.
Parameter | Info
--------- | ----
nobuttons | Removes up & down buttons
autohide_buttons | Automatically removes up & down buttons when not needed
Slider{} | ControlName: ScrollBarSlider
UpButton{} | ControlName: ScrollBarButton
DownButton{} | ControlName: ScrollBarButton

Default scheme values
Font | Color | Border | Other
---- | ----  | ------ | -----
   |   |   | ScrollBar.Wide


## ScrollBarSlider
The slider of a scrollbar. Derives from Panel.
Parameter | Info
--------- | ----
ButtonBorder | Border of the slider. Only works with IgnoreScheme 1

Default scheme values
Font | Color | Border
---- | ----  | ------
   | ScrollBarSlider.FgColor | ScrollBarSliderBorder
   | ScrollBarSlider.BgColor | ButtonBorder


## ScrollBarButton
Derives from Button.

Default scheme values
Font | Color | Border
---- | ----  | ------
 Marlett | ScrollBarButton.FgColor | ScrollBarButtonBorder
   | ScrollBarButton.BgColor | ScrollBarButtonDepressedBorder
   | ScrollBarButton.ArmedFgColor | 
   | ScrollBarButton.ArmedBgColor | 
   | ScrollBarButton.DepressedFgColor | 
   | ScrollBarButton.DepressedBgColor | 


## CExScrollBar
"A scroll bar that can have specified width" (?)


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
rotation | Rotate image in 90 degree increments
positionImage


## ScalableImagePanel
A panel that displays an image. Can have scalable corners & sides. Derives from Panel.
Parameter | Info
--------- | ----
image | The image to display
drawcolor | What colour to draw the image with
src_corner_width | How big the texture's corners are in the X axis
src_corner_height | How big the texture's corners are in the Y axis
draw_corner_width | How big to draw the corners in the X axis
draw_corner_height | How big to draw the corners in the Y axis


## CTFImagePanel
An image panel that can be team coloured. Derives from ScalableImagePanel
Parameter | Info
--------- | ----
teambg_0 | Image when unassigned
teambg_1 | Image on spectate
teambg_2 | Image on RED
teambg_3 | Image on BLU


## CIconPanel
A panel that displays an icon from scripts/mod_textures.txt. Derives from Panel.
Parameter | Info
--------- | ----
icon | What icon to use
iconColor | What colour to draw the icon with
scaleImage | Should the icon scale with the panel


## CAvatarImagePanel
Derives from Panel.
Parameter | Info
--------- | ----
scaleImage
color_outline


## CBitmapPanel
Parameter | Info
--------- | ----
material | Looks in materials/ instead of materials/vgui/
color


## CBitmapImagePanel
An image that can maintain its aspect ratio when resized. Derives from Panel.
Parameter | Info
--------- | ----
image | The image to display
imagecolor | What colour to draw the image with
imageAlignment | Where the image should align
preserveAspectRatio | Should the aspect ratio be maintained
filtered


## CTFLogoPanel
A rotating TF logo.
Parameter | Info
--------- | ----
radius | Size of the logo
velocity | Speed of the logo



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
disabledFgColor_override
disabledBgColor_override
selectionColor_override
selectionTextColor_override
defaultSelectionBG2Color_override

Default scheme values
Font | Color | Border
---- | ----  | ------
 Default | TextEntry.TextColor | ButtonDepressedBorder
 DefaultVerySmall | TextEntry.BgColor | 
   | TextEntry.CursorColor | 
   | TextEntry.DisabledTextColor | 
   | TextEntry.DisabledBgColor | 
   | TextEntry.SelectedTextColor | 
   | TextEntry.SelectedBgColor | 
   | TextEntry.OutOfFocusSelectedBgColor | 
   | TextEntry.FocusEdgeColor | 


## ComboBox
A panel with a drop down list. Derives from TextEntry.
Parameter | Info
--------- | ----
border_override | Changes the border
Button{} | ControlName: ComboBoxButton

Default scheme values
Font | Color | Border
---- | ----  | ------
   |   | ComboBoxBorder

## ComboBoxButton
Derives from Button.

Default scheme values
Font | Color | Border
---- | ----  | ------
 Marlett | ComboBoxButton.ArrowColor | ScrollBarButtonBorder
   | ComboBoxButton.BgColor | 
   | ComboBoxButton.ArmedArrowColor | 
   | ComboBoxButton.DisabledBgColor | 
   


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

Default scheme values
Font | Color | Border
---- | ----  | ------
 DefaultVerySmall | Slider.NobColor | ButtonBorder
   | Slider.TextColor | ButtonDepressedBorder
   | Slider.TrackColor | 
   | Slider.DisabledTextColor1 | 
   | Slider.DisabledTextColor2 | 


## CCVarSlider
A slider that can change a cvar. Derives from Slider
Parameter | Info
--------- | ----
minvalue | Minimum value allowed
maxvalue | Maximum value allowed
cvar_name | Cvar to change
use_convar_minmax | Use the minvalue & maxvalue of the cvar instead
allowoutofrange


## ProgressBar
A segmented progress bar. Derives from Panel.
Parameter | Info
--------- | ----
variable | What to measure
progress


## ContinuousProgressBar
Derives from ProgressBar.


## CBuildingHealthBar
A progress bar that changes colour when below 50%. Derives from ProgressBar.

Default scheme values
Font | Color | Border
---- | ----  | ------
   | BuildingHealthBar.BgColor | 
   | BuildingHealthBar.Health | 
   | BuildingHealthBar.LowHealth | 


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


## CAccountPanel
Derives from EditablePanel.
Parameter | Info
--------- | ----
delta_item_start_y
delta_item_end_y
delta_item_x
delta_item_end_x
bg_texture
bg_image_x
bg_image_y
bg_image_wide
bg_image_tall
PositiveColor
NegativeColor
EventColor
RedRobotScoreColor
BlueRobotScoreColor
delta_lifetime
delta_item_font
delta_item_font_big
negative_flip_dir


## CModelPanel
A panel that shows a 3D model. Derives from EditablePanel.
Parameter | Info
--------- | ----
fov | FOV of the model
start_framed
allow_offscreen
model{}

The following parameters need to be in model{}
Parameter | Info
--------- | ----
modelname | What model to use
modelname_hwm
skin | Which skin to use
angles_x | Rotation around X axis
angles_y | Rotation around Y axis
angles_z | Rotation around Z axis
origin_x | Position in the X axis
origin_y | Position in the Y axis
origin_z | Position in the Z axis
frame_origin_x
frame_origin_y
frame_origin_z
vcd
spotlight
animation{} | Animations of the model
attached_model{} | Attach another model eg. a gun

The following parameters need to be in animation{}
Parameter | Info
--------- | ----
name 
sequence
activity
default
pose_parameters{}

The following parameters need to be in attached_model{}
Parameter | Info
--------- | ----
modelname
skin


## CPotteryWheelPanel
Derives from EditablePanel.
Parameter | Info
--------- | ----
useparentbg
lights{}

The following parameters need to be in lights{}
Parameter | Info
--------- | ----
name | Accepts "directional", "point" or "spot"
color
direction | directional & spot
attenuation | point & spot
origin | point & spot
maxDistance | point & spot
inner_cone_angle | spot
outer_cone_angle | spot
exponent | spot

```
"lights"
{
	"1"
	{
		"name"	"directional"
		"color"	"10 10 10"
		"direction" "0 0 0"
	}
}
```


## CMDLPanel
Derives from CPotteryWheelPanel.


## CBaseModelPanel
Derives from CMDLPanel
Parameter | Info
--------- | ----
render_texture
use_particle
start_framed
disable_manipulation
fov
allow_rot
allow_pitch
allow_manip
max_pitch
model{}

The following parameters need to be in model{}
Parameter | Info
--------- | ----
force_pos
modelname | What model to use
modelname_hwm
skin | Which skin to use
angles_x | Rotation around X axis
angles_y | Rotation around Y axis
angles_z | Rotation around Z axis
origin_x | Position in the X axis
origin_y | Position in the Y axis
origin_z | Position in the Z axis
frame_origin_x
frame_origin_y
frame_origin_z
vcd
spotlight
animation{} | Animations of the model
attached_model{} | Attach another model eg. a gun

The following parameters need to be in animation{}
Parameter | Info
--------- | ----
name 
sequence
activity
default
pose_parameters{}

The following parameters need to be in attached_model{}
Parameter | Info
--------- | ----
modelname
skin


## CTFPlayerModelPanel
Derives from CBaseModelPanel.
Parameter | Info
--------- | ----
disable_speak_event |
customclassdata{} | Allows you to set fov, origin and angles for each class individually


## CItemModelPanel
A panel that show an item. Derives from EditablePanel.
Parameter | Info
--------- | ----
special_attributes_only
model_xpos | Position of the model in the X axis
model_ypos | Position of the model in the Y axis
model_wide | Wide of the model
model_tall | Tall of the model
model_center_x | Center the model in the X axis
model_center_y | Center the model in the Y axis
tf2_icon_offset_x
tf2_icon_offset_y
noitem_use_fullpanel
text_center | Center the text in the Y axis
text_center_x | Center the text in the X axis
use_item_sounds
name_only | Don't show the stats of the item
attrib_only | Don't show the name of the item
model_only | Don't show the name or the stats of the item
model_hide | Don't show the model
paint_icon_hide
resize_to_text 
name_label_alignment
text_xpos | Position of the text in the X axis
text_ypos | Position of the text in the Y axis
text_wide | Wide of the text
text_yoffset
padding_height
max_text_height
text_forcesize
inset_eq_x | Equipped label X position
inset_eq_y | Equipped label Y position
standard_text_color
is_mouseover
wide
tall
collection_list_xpos
text_xpos_collection
hide_collection_panel
hide_modifier_icons


## CEmbeddedItemModelPanel
Model panel inside CItemModelPanel. Derives from CBaseModelPanel.
Parameter | Info
--------- | ----
force_use_model
use_item_rendertarget
inventory_image_type
force_square_image
model_rotate_yaw_speed
use_pedestal


## CTFParticlePanel
A panel that displays a particle effect. Derives from EditablePanel.
Parameter | Info
--------- | ----
ParticleEffects{}

The following parameters need to be in ParticleEffects{}
Parameter | Info
--------- | ----
particle_xpos | X position of the particle
particle_ypos | Y position of the particle
particle_scale | Scale of the prticle
loop | Loop the particle animation
start_activated | Activate the particle animation immediately
particleName | Name of the particle
angles | Rotation of the particle, takes 3 values
control_point* | Particle control point setting, takes 3 values. Replace * with the number of the control point

```
"ParticleEffects"
{
	"1"
	{
		"particle_xpos"	"0"
		"particle_ypos"	"0"
		"particle_scale"	"1.0"
		"loop"			"1"
		"start_activated"	"1"
		"particleName"	""
		"angles"		"0 0 0"
		"control_point0"	"4 2 0"
		"control_point1"	"6 9 6"
	}
}
```


## CDrawingPanel
A panel you can draw in. Derives from Panel.
Parameter | Info
--------- | ----
linecolor | What colour the line should be
team_colors | Use team colours for the line


## CNavigationPanel
A panel that has a list of buttons. The command for the buttons is select_0, select_1, select_2 etc. The commands can be aliased to something else. Derives from EditablePanel.
Parameter | Info
--------- | ----
auto_layout
auto_scale
display_vertically
auto_layout_horizontal_buffer
auto_layout_vertical_buffer
selected_button_default
ButtonSettings{} | Settings for the buttons to use
Buttons{} | List of buttons


## CTFVideoPanel
Parameter | Info
--------- | ----
command
start_delay
end_delay


## CTFArrowPanel
Derives from Panel.
Parameter | Info
--------- | ----


## CTFPlayerPanel 
Derives from EditablePanel.
Parameter | Info
--------- | ----
HealthIcon{} | ControlName: CTFPlayerPanelGUIHealth
ReadyBG{} | ControlName: ScalableImagePanel
ReadyImage{} | ControlName: ImagePanel



## CTFTeamStatus
Derives from EditablePanel.
Parameter | Info
--------- | ----
team1_grow_dir
team2_grow_dir
max_size
6v6_gap
12v12_gap
team1_base_x
team1_max_expand
team2_base_x
team2_max_expand
playerpanels_kv{}


## CTFTeamStatusPlayerPanel
Derives from CTFPlayerPanel.
Parameter | Info
--------- | ----
color_portrait_bg_red_local_player
color_portrait_bg_blue_local_player
color_portrait_bg_red
color_portrait_bg_blue
color_portrait_bg_red_dead
color_portrait_bg_blue_dead
color_bar_health_high
percentage_health_med
color_bar_health_med
percentage_health_low
color_bar_health_low
color_portrait_blend_dead_red
color_portrait_blend_dead_blue
healthbar{} | ControlName: ContinuousProgressBar
overhealbar{} | ControlName: ContinuousProgressBar
classimagebg{} | ControlName: Panel
DeathPanel{} | ControlName: ImagePanel


## CTFHudPlayerHealth
Derives from EditablePanel.
Parameter | Info
--------- | ----
HealthBonusPosAdj
HealthDeathWarning
HealthDeathWarningColor



## CTFSpectatorGUIHealth
Derives from CTFHudPlayerHealth.



## CTFPlayerPanelGUIHealth
Derives from CTFSpectatorGUIHealth.



## CPvPRankPanel
Derives from EditablePanel.
Parameter | Info
--------- | ----
matchgroup | MatchGroup_Ladder_6v6 or MatchGroup_Casual_12v12
show_type
show_name
show_model
show_progress
instantly_update
show_sources_when_hidden
xp_source_notification_center_x


## CMiniPvPRankPanel
Derives from CPvPRankPanel.


## CDashboardPartyMember
Parameter | Info
--------- | ----
party_slot


## CMVMCriteriaPanel
Parameter | Info
--------- | ----
challenge_spacer
challenge_name_width
challenge_skill_width
challenge_completed_size
challenge_map_width
challenge_map_height
has_ticket_width
squad_surplus_width
squad_surplus_width
badge_level_width
tour_name_width
tour_skill_width
tour_progress_width
tour_number_width


## CExplanationPopup
A speech bubble panel. Accepts button commands "close", "nextexplanation" & "prevexplanation". Derives from EditablePanel.
Parameter | Info
--------- | ----
next_explanation | Next speech bubble to draw
force_close | Disable the rest of the screen until this popup is closed
callout_inparents_x | X position of the speech bubble's tail
callout_inparents_y | Y position of the speech bubble's tail
start_x | X position before the expanding animation
start_y | y position before the expanding animation
start_wide | Wide before the expanding animation
start_tall | Tall before the expanding animation
end_x | X position after the expanding animation
end_y | y position after the expanding animation
end_wide | Wide after the expanding animation
end_tall | Tall after the expanding animation


## CRepeatingContainer
A panel that automatically positions its contents. Derives from EditablePanel.
Parameter | Info
--------- | ----
spacing_method | How to space the panels. METHOD_STEP spaces them by a certain value, METHOD_EVEN spaces them evenly
x_step | Value to space the panels when using METHOD_STEP
IndividualSettings{} | Where you place the panels to be sorted
CommonSettings{} | What settings the panels should have by default

```
"Example"
{
  "ControlName"  "CRepeatingContainer"

  "IndividualSettings"
  {
    "Item1"
    {
      "ControlName"  "Label"
    }
    "Item2"
    {
      "ControlName"  "Label"
    }
    "Item3"
    {
      "ControlName"  "Label"
    }
  }

  "CommonSettings"
  {
    "fgcolor_override"  "69 69 69 255"
    "font"              "Default"
  }
}
```

## CLoadoutPresetPanel
Derives from EditablePanel
Parameter | Info
--------- | ----
presetbutton_kv{}


## CCyclingAdContainerPanel
Derives from EditablePanel
Parameter | Info
--------- | ----
items{}


## CItemAdPanel
Derives from EditablePanel
Parameter | Info
--------- | ----
item
show_market
present_time


## CBuildingStatusAlertTray
Derives from Panel.
Parameter | Info
--------- | ----
icon
deployed | Float 0.0 - 1.0


## CTFItemCardPanel
A leftover unused panel that uses Resource/UI/Econ/ItemCardPanel_Series1.res for its contents. Could be useful for a #base -esque reusable panel. Derives from EditablePanel
Parameter | Info
--------- | ----
shadowoffset




