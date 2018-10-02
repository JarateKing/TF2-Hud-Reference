import os
import glob

# directories
existing_file = "TESTLIST.md" # os.path.abspath("../2-LISTS/Filelist.md")
reference_folder = "../reference/"

# get all filenames
existing = []
current_path = ""
f = open(existing_file, "r")
for line in f:
	if "#" not in line:
		if " | " in line and "File | Description" not in line and "---- | " not in line:
			existing.append(current_path + line)
	else:
		if "/" in line:
			current_path = line.replace("## ","").replace("\n","")
f.close()

# get all files
tocheck = []
for file in glob.glob(reference_folder + "**/*", recursive=True):
	current = file.replace("\\","/").replace(reference_folder,"")
	if "." in current:
		tocheck.append(current)

# debug
for line in tocheck:
	print(line)

# end program
input("press Enter to continue")