# Useful Commands

There are many useful console commands to use in hud editing.

## `hud_reloadscheme`

An extremely common command used in hud development, this allows you to reload the hud while ingame. It has several limitations however, since it does not reload the clientscheme, and doesn't reload most menu elements. It is recommended to set `vgui_cache_res_files` to 0 when trying to reload hud files.

## `toggle mat_antialias 0 1`

Changing the value of `mat_antialias` achieves a result similar to `hud_reloadscheme`, except it also reloads the majority of menu elements (but still doesn't reload the clientscheme). It also reloads all materials, and predictably takes longer, as well as changes overall visual quality of TF2. This is mostly useful when editing elements such as the main menu, which don't reload when you use `hud_reloadscheme`.

Note that by default mastercomfig blocks the `mat_antialias` command. You can prevent that, by adding `alias block_antialias` to your `user/autoexec.cfg` file.

## `vgui_drawtree 1`

`vgui_drawtree` is a command that allows you to see the name and some details on every hud element currently rendered. Recommended to change `vgui_drawtree_draw_selected` to 1 (or tick the box for *Highlight Selected* in the VGUI Hierarchy window), to highlight your selected on screen hud item when traversing through the tree with hud elements.

## `showschemevisualizer <scheme>`

Shows the colors, borders, and fonts that a scheme file defines. It can either take no argument (which will show the clientscheme) or an argument for the scheme name.

As a list of valid schemes:
```
showschemevisualizer sourcescheme
showschemevisualizer sourceschemebase
showschemevisualizer chatscheme
showschemevisualizer videopanelscheme
```

## `cc_emit <caption>`

Emits a caption, giving the caption name as an argument. Both useful for testing captions, and developing unique hud features (such as custom scripting menus) with captions.

## `hurtme <value>`

Damages or heals the player. Positive numbers damage the player by that much, negative numbers heal the player by that much. Useful for testing health values and [animations](https://github.com/JarateKing/TF2-Hud-Reference/blob/master/0-TUTORIAL/4-Editing-Animations.md).

## `cl_hud_minmode <0/1>`

Determines whether to use variables that end in `_minmode` if present, or the default otherwise.
