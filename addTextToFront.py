import os
import sys

# String to be added
stri = ""
# If we want to filter by file extension
filt = ""
if(len(sys.argv) > 1):
	stri = sys.argv[1]
	if(len(sys.argv) > 2):
		filt = sys.argv[2]

	path = os.getcwd()
	
	for root, directories, file in os.walk(path):
		for file in file:
			if(file.endswith(filt)):
				os.rename(path + "/" + file, path + "/" + stri + file)