# Operating System Tags

There are several operating system tags that are in-use, that allow you to specify that an attribute only applies for a specific operating system.

An example of tags in use is:
```
"xpos"			"25"	[$WIN32]
"xpos"			"57"	[$X360]
```

## List of Tags

Tag | Function
--- | --------
`[$WIN32]` | For PC / non-console. Not just Windows, but also Mac and Linux
`[$X360]` | For console.
`[$WINDOWS]` | For Windows specifically.
`[$OSX]` | For Mac specifically.
`[$LINUX]` | For Linux specifically.
`[$POSIX]` | For either Mac or Linux.

It's important to note that `[$WIN32]` is not opposite of `[$OSX]` or `[$LINUX]`, which is a common misconception. A linux machine will attempt to use any attribute with the tags `[$LINUX]`, `[$POSIX]`, or `[$WIN32]`.

These can be useful because not every operating system renders things the same. Refer to the [linux support appendix](./LinuxSupport.md) for an example.
