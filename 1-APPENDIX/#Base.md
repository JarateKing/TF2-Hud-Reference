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