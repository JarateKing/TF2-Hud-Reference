import os
import glob

# directories
existing_file = os.path.abspath("../2-LISTS/Filelist.md")
reference_folder = "../reference/"

# iterate over description method
count = 0
descriptions = []
def getDescription():
	global count
	toRet = "###table"
	if count < len(descriptions):
		toRet = descriptions[count]
	count += 1
	return toRet

# get the previous descriptions from the existing file list
existing = []
current_path = ""
try:
	f = open(existing_file, "r")
	for line in f:
		if "##" not in line:
			if " |" in line and "File | Description" not in line and "---- | " not in line:
				existing.append(current_path + line.strip())
			elif "File | Description" in line:
				descriptions.append("###table")
			elif "---- | -----------" not in line:
				descriptions.append(line.strip())
		elif "/" in line:
				current_path = line.replace("## ","").strip()
				descriptions.append("###" + current_path)
		else:
			descriptions.append(line.strip())
	f.close()
except:
	pass

# get all files
tocheck = []
folderlist = ["scripts/", "resource/"] # to specify order
for subfolder in folderlist:
	for file in glob.glob(reference_folder + subfolder + "**/*", recursive=True):
		current = file.replace("\\","/").replace(reference_folder,"")
		if "." in current:
			tocheck.append(current)

# bring them together, with descriptions
combined = []
current_path = ""
for file in tocheck:
	toAdd = ""
	path = "/".join(file.split("/")[0:-1])
	if path != current_path:
		current_path = path
		current_string = getDescription()
		while ("###" not in current_string):
			combined.append(current_string)
			current_string = getDescription()
		if (count > len(descriptions)):
			combined.append("")
		combined.append("## " + path + "/")
		current_string = getDescription()
		while ("###" not in current_string):
			combined.append(current_string)
			current_string = getDescription()
		if (count > len(descriptions)):
			combined.append("")
		combined.append("File | Description")
		combined.append("---- | -----------")
	
	for line in existing:
		if line.split(None, 1)[0] == file:
			toAdd = line
	if toAdd == "":
		combined.append(file.replace(path + "/", "") + " | ")
	else:
		combined.append(toAdd.replace(path + "/", ""))

# print out what the file will be
for line in combined:
	print(line)

# verify that all is good
input("VERIFY THAT THIS IS PROPER, PRESS ENTER TO OVERWRITE FILE")

# write to file
f = open(existing_file, "w")
for line in combined:
	f.write(line + '\n')

# end the program
print("Success!")
input("Press Enter to exit the program")