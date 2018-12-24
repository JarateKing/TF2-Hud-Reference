import os
import glob

# directories
existing_file = os.path.abspath("../2-LISTS/Statlist.md")
reference_folder = "../reference/"

# get all files
files = []
folderlist = ["scripts/", "resource/"] # to specify order
for subfolder in folderlist:
	for file in glob.glob(reference_folder + subfolder + "**/*", recursive=True):
		current = file.replace("\\","/").replace(reference_folder,"")
		if "." in current:
			files.append(current)

combined = []
current_path = ""
for file in files:
	path = "/".join(file.split("/")[0:-1])
	if path != current_path:
		combined.append("## " + path + "/")
		current_path = path
	
	combined.append(file.replace(path + "/", ""))
	
for line in combined:
	print(line)
	
print("Success!")
input("Press Enter to exit the program")