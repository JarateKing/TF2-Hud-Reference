# Refract Materials

Refracts are a type of material that can be used in a few ways for unique purposes.

## Understanding Refracts

To begin with, it's important to understand what a refract is and why it works the way it does. In a general sense, a refract is a material that can warp the view world geometry, depending on its strength and the uv material used. For example, this is used in tf2 for underwater effects or when jarate'd, to distort your view of the world.

In huds, the strength will almost always be 0. This means that there is no warping, and now you have a material that is (mostly) identical to your view of the map. Beyond this it's a regular material, and can still be affected by many vmt properties or proxies.

## Hud Masking

The most immediate use of refracts is to cover up hud elements. Because they draw the world view under it, covering up a hud element with a refract will effectively hide that element. The interesting use of this is to partially hide a hud element, either by making a refract that is smaller than the hud element, or by having the refract's uv map make a shape to 'cut out' (for example, if the refract's uv map is a circle, then putting it over a square will cut out that circle from the square).

## Blurs

Similar to hud masking, you can also make the refract material blur. This creates a "frosted glass" effect.