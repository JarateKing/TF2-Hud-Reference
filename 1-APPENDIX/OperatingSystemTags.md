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
