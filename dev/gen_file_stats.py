import os
import glob
import re

# directories
existing_file = os.path.abspath("../2-LISTS/Statlist.md")
reference_folder = "../reference/"
header_file = "stat_list_header.md"

# get all files
files = []
folderlist = ["scripts/", "resource/"] # to specify order
for subfolder in folderlist:
	for file in glob.glob(reference_folder + subfolder + "**/*", recursive=True):
		current = file.replace("\\","/").replace(reference_folder,"")
		if "." in current:
			files.append(current)

combined = []

headerfile = open(header_file, "r")
for line in headerfile:
	combined.append(line.replace("\n", ""))
headerfile.close()

current_path = ""
for file in files:
	path = "/".join(file.split("/")[0:-1])
	if path != current_path:
		current_path = path
		combined.append("## " + path + "/")
		combined.append("Filename | linecount | minmode | #base | if_mvm")
		combined.append("-------- | --------- | ------- | ----- | ------")
		
	count_lines = 0
	count_minmode = 0
	count_base = 0
	count_mvm = 0
	
	searchfile = open(reference_folder + file, "r")
	try:
		for line in searchfile:
			count_lines += 1
			count_minmode += len(re.findall(r"_minmode", line.lower()))
			count_base += len(re.findall(r"#base ", line.lower()))
			count_mvm += len(re.findall(r"if_mvm", line.lower()))
	except:
		pass
	searchfile.close()
	
	filename = file.replace(path + "/", "")
	combined.append(filename + " | " + str(count_lines) + " | " + str(count_minmode) + " | " + str(count_base) + " | " + str(count_mvm))
	combined[-1] = combined[-1].replace(" 0", "")
	
for line in combined:
	print(line)
	
# verify that all is good
input("VERIFY THAT THIS IS PROPER, PRESS ENTER TO OVERWRITE FILE")

# write to file
f = open(existing_file, "w")
for line in combined:
	f.write(line + '\n')
	
print("Success!")
input("Press Enter to exit the program")