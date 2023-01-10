import os
import sys

path = os.getcwd()

output = [
	"Remove Extension",
	"Add Extension",
	"Add Text to the front",
	"Remove Text from the back (excluding Extension)"
]

i = 1
for o in output:
	print("{0}. {1}".format(i, o))
	i += 1

# Ignore everything after the first char
s = int(input("\nWhat do you choose?\n")[0])

if(s <= 0 or s >= len(output) + 1):
	raise Exception("Invalid Choice")

print("\nYou Chose '{0}'".format(output[s - 1]))

counter = 0

if s == 1:
	filt = "." + input("Do you want to remove a particular type of extension? Type cpp to filter '.cpp' ")
	for root, directories, file in os.walk(path):
		for file in file:
			if file != "fileManager.py" and file.find(filt) != -1:
				fsplit = file.split(".")
				d = len(fsplit[1]) + 1
				os.rename(path + "/" + file, path + "/" + file[:-d])
				counter += 1
elif s == 2:
	ext = input("What extension do you want to add? Type cpp to add '.cpp' ")
	# Filters leading .
	if(ext[0] == "." and len(ext) > 1):
		ext = ext[1:]
	
	# Checks if the extension onyl contains letters
	if not ext.isalpha():
		raise Exception("Extension must only contain letters.")

	if len(ext) > 6:
		raise Exception("Extension must not be longer than 6 characters")

	if len(ext) == 0:
		raise Exception("Empty string")

	for root, directories, file in os.walk(path):
		for file in file:
			if not "." in file:
				os.rename(path + "/" + file, path + "/" + file + "." + ext)
				counter += 1
elif s == 3:
	stri = input("What string do you want to add?\n")
	filt = input("Do you want to filter by Extension? Type cpp to filter for '.cpp', leave blank otherwise.\n")
	for root, directories, file in os.walk(path):
		for file in file:
			if file != "fileManager.py" and file.endswith(filt):
				os.rename(path + "/" + file, path + "/" + stri + file)
				counter += 1
elif s == 4:
	inp = int(input("How many letters do you want to remove? "))
	if inp > 0:
		for root, directories, file in os.walk(path):
			for file in file:
				if file != "fileManager.py":	
					fsplit = file.split(".")
					if(len(fsplit) > 1):
						ext = "." + fsplit[1]
					else:
						ext = ""
					
					if len(fsplit[0]) <= inp:
						print("Filename is too short for {0}".format(fsplit[0] 	+ ext))
					else:
						print("")
						os.rename(path + "/" + file, path + "/" + fsplit[0][:-inp] + ext)
						counter += 1

if counter > 0:
	print("Successfully changed {0} entries!".format(counter))