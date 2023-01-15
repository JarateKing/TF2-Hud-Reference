# Basefile Script Integration

Through a clever use of `#base` and echo logging, we can swap out resource files arbitrarily.

First, let's setup our hud files like so:

```
resource/ui/hudplayerhealth_def.res
resource/ui/hudplayerhealth_alt.res
```

Where `def` is the default `hudplayerhealth` that we'd like to use, and `alt` is an alternate option for this file.

Lets create a `hudplayerhealth.res` that uses `#base`:

```
#base "../../cfg/hud_hudplayerhealth.txt"
#base "hudplayerhealth_def.res"

"Resource/UI/HudPlayerHealth.res"
{	
}
```

This will attempt to load a file (that currently doesn't exist!) in `cfg` called `hud_hudplayerhealth.txt` and apply the contents of that file, and if that file doesn't exist or is empty, will then apply the contents of `hudplayerhealth_def.res` (our default hud file).

We can use scripts to write to `cfg/hud_hudplayerhealth.txt` so that it will use `resource/ui/hudplayerhealth_alt.res` when we run a script. We setup our script like so:

```
alias hudplayerhealth_clear "sixense_clear_bindings; sixense_write_bindings hud_hudplayerhealth.txt"
alias hudplayerhealth_log "con_filter_text #base; con_filter_enable 1; con_logfile cfg/hud_hudplayerhealth.txt"
alias hudplayerhealth_unlog "con_logfile console.log"

alias hudplayerhealth_alt "hudplayerhealth_clear; hudplayerhealth_log; exec hud/hudplayerhealth_alt.cfg; hudplayerhealth_unlog; hud_reloadscheme"
alias hudplayerhealth_def "hudplayerhealth_clear; hud_reloadscheme"
```

With another file `hud/hudplayerhealth_alt.cfg` as well:
```
echo "#base ../resource/ui/hudplayerhealth_alt.res"
```

With this in place, when we run `hudplayerhealth_alt` in console, our hud will switch to using `hudplayerhealth_alt.res` as our `hudplayerhealth.res` file. We can also run `hudplayerhealth_def` to use `hudplayerhealth_def.res` again. This change will persist even after closing TF2.

The same concept can be expanded arbitrarily: we could have a setup with multiple options, where we'd just use the same setup as above but have multiple different variations of the `hudplayerhealth_alt` alias and different `hud/hudplayerhealth_alt.cfg` files it uses to echo. Nor is there anything limiting it to `hudplayerhealth.res`, the same concept could function with any `.res` file (files like `mainmenuoverride.res` may require using a different method of reloading the hud, however).
