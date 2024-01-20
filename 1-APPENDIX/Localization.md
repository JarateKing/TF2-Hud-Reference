# Localization

Localization is loaded through various files. The load order of these files is:

1. replay_english
2. youtube_english
3. valve_english
4. gameui_english
5. valve_english (again)
6. platform_english
7. vgui_english
8. tf_english
9. chat_english
10. closecaption_english
11. tf_proto_obj_defs_english
12. serverbrowser_english

When entering a map, `mapname_english` will also get loaded.

As well as loading `closecaption_english`, the game will also load whatever you have your `cc_lang` set to. For example, with `cc_lang test`, it will load both `closecaption_english` and `closecaption_test`. When you change `cc_lang`, it will also load that localization file mid-game. This can be used to, during gameplay, change any existing localization (or add new ones) by loading arbitrary localization files. Keep in mind that this will also change the captions being used.

## Format

An example file (`chat_english.txt`) looks like:

```
"lang"
{
"Language" "English"
"Tokens"
{
"chat_filterbutton"	"Filters"
"filter_joinleave"	"Joins/Leaves"
"filter_namechange"	"Name Changes"
"filter_publicchat"	"Public Chat"
"filter_servermsg"	"Server Messages"
"filter_teamchange"	"Team Changes"
"filter_achievement" "Achievement Announce"
"chat_say"				"Say :"
"chat_say_team"			"Say (TEAM) :"
"chat_say_party"		"Say (PARTY) :"
}
}
```

Some points with the format:
* this file must be encoded in UCS-2 LE BOM. The easiest method is to copy over an existing localization file. You can set this in notepad++'s "Encoding" dropdown menu.
* `Language` can be set to anything, the `"English"` is never actually used in tf2
* the list of tokens is the actual localization strings, as a pair of keys and values

## Usage

To use a localized string, you would set the labeltext of a string to be `#key` where key is whatever the left string is in the localization file. For example, you would use `"#chat_say"` if you wanted the string associated with that key.

Localization has a secondary benefit, where directly setting the labeltext of a label to `%health% %health%` won't work as you intended, and will print those strings literally instead of `125 125` as you might expect. This does not apply for localized strings, where `"doublehp" "%health% %health%"` in a localization file and a label with `"#doublehp"` as its labeltext will work.
