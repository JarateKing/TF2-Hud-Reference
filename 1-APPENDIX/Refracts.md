# Refract Materials

Refracts are a type of material that can be used in a few ways for unique purposes.

They take the form of:
```
"Refract"
{
	"$refractamount" "0.0"
	"$refracttint" "{255 255 255}"
	"$refractblur" "0.0"
	"$normalmap" "vgui/replay/thumbnails/refract/basic"
	
	<dx90
	{
		 	"$fallbackmaterial" "vgui/replay/thumbnails/fallback"
	}
}
```

Certain commands should be used with refracts as well, namely:
```
// force refracts to work on the hud immediately
// otherwise you will need to be jarate'd / bleed / go underwater
mat_motion_blur_enabled 1

// improve visual quality with refracts
mat_motion_blur_strength 0
mat_disable_bloom 1
mat_hdr_level 0
mat_antialias 0
mat_colcorrection_disableentities 1
mat_colorcorrection 0
```

Some notes:
* the <dx90 fallback part is because refracts are not supported in dx8.
* refracttint is the color that the refract should take.
* the hud element's alpha value doesn't affect refracts. You have to edit the normal map vtf to change its alpha.

## Understanding Refracts

To begin with, it's important to understand what a refract is and why it works the way it does. In a general sense, a refract is a material that can warp the view world geometry, depending on its strength and the normal map used. For example, this is used in tf2 for underwater effects or when jarate'd, to distort your view of the world.

In huds, the strength will almost always be 0. By consequence, the color values of the normal map don't matter, only the alpha values in the normal map matters. This means that there is no warping, and now you have a material that is (mostly) identical to your view of the map. Beyond this it's a regular material, and can still be affected by many vmt properties or proxies.

## Hud Masking

The most immediate use of refracts is to cover up hud elements. Because they draw the world view under it, covering up a hud element with a refract will effectively hide that element. The interesting use of this is to partially hide a hud element, either by making a refract that is smaller than the hud element, or by having the refract's normal map make a shape to 'cut out' (for example, if the refract's normal map is a circle, then putting it over a square will cut out that circle from the square).

## Blurs

Similar to hud masking, you can also make the refract material blur. This creates a "frosted glass" effect.

## Transparent Viewmodels

With certain settings, viewmodels are excluded from refracts. This is beneficial, because now refracts can mask the viewmodel as well. With a transparent refract, covering up the viewmodel will make the viewmodel appear transparent.

## Filters

By changing the refracttint value in the vmt, you can create a filter that only allows certain colors to pass through. In other words, apply multiplicative blending (with 255 being 1.0) to the world. For example:
```
	"$refracttint" "{255 127 0}"
```
Will allow red to appear like normal, blue to appear as black, green to appear as dark green, and white to appear as an orange color.