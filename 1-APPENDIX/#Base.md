# #Base files

Using #base allows a file to be loaded in, and provide a 'default' for the current file--any value that is not overridden in the regular file but does exist in the #base file, will have the #base file's value used. The same logic applies for elements in the #base file but not in the regular file.

## Example

Inside the default hud, sourcescheme.res demonstrates a #base being used.
```
#base "SourceSchemeBase.res"

Scheme
{
...
```

Note that this loads a file named "SourceSchemeBase.res" inside the current directory. The #base file's path is always relative to the regular file, and can be loaded by changing the path.

## Load Order

There can be multiple #base files loaded just fine. Like so:
```
#base "file_one.res"
#base "file_two.res"
#base "file_three.res"
```
Because multiple files can all have different values for the same parameters, the order of these is important. If there are any conflicts like this, the first file loaded will be used.

## Stub files

Some huds will choose to move all the default contents into a #base file, and load changes from other #base files. For example:
```
#base "../resource/ui/custom/damageindicator.res"
#base "../resource/ui/custom/killfeed.res"
#base "../resource/ui/custom/closecaptions.res"

#base "base/hudlayout.res"

"Resource/HudLayout.res"
{
}
```
The main advantages of this are that everything is separated into their own files easier, and things are easier to update by just changing the #base default file. Some huds will even have a script to extract the default file from the tf2 VPK files and place it to be loaded from #base to potentially make updating completely automatic (though some changes can still break it).