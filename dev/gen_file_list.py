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
			existing.append(current_path + line.strip())
	else:
		if "/" in line:
			current_path = line.replace("## ","").strip()
f.close()

# get all files
tocheck = []
for file in glob.glob(reference_folder + "**/*", recursive=True):
	current = file.replace("\\","/").replace(reference_folder,"")
	if "." in current:
		tocheck.append(current)

# bring them together
combined = []
current_path = ""
for file in tocheck:
	toAdd = ""
	path = "/".join(file.split("/")[0:-1])
	if path != current_path:
		current_path = path
		combined.append("")
		combined.append("## " + path + "/")
		combined.append("")
	
	for line in existing:
		if line.split(None, 1)[0] == file:
			toAdd = line
	if toAdd == "":
		combined.append(file.replace(path + "/", "") + " | ")
	else:
		combined.append(toAdd.replace(path + "/", ""))

# debug
for line in combined:
	print(line)

# end program
input("press Enter to continue")