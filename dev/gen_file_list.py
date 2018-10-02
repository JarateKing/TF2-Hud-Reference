import os

# get all filenames
existing = []
f = open(os.path.abspath("../2-LISTS/Filelist.md"), "r")
for line in f:
	existing.append(line)
f.close()

# debug
for line in existing:
	print(line)

# end program
input("press Enter to continue")