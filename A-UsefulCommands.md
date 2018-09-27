# Useful Commands

There are many useful console commands to use in hud editing.

## hud_reloadscheme

An extremely common command used in hud development, this allows you to reload the hud while ingame. It has several limitations however, since it does not reload the clientscheme, and doesn't reload most menu elements.

## toggle mat_antialias 0 1

Similar to hud_reloadscheme, except it also reloads the majority of menu elements (but still doesn't reload the clientscheme). It also reloads all materials, and predictably takes longer, as well as changes overall visual quality of tf2.

## vgui_drawtree

vgui_drawtree is a command that allows you to see the name and some details on every hud element currently rendered.