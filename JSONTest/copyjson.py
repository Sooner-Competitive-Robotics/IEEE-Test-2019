import glob, os
from shutil import copyfile

def copyjson():
	for subdir in os.listdir("/home/media"):
		subdirpath = "/home/media/"+subdir;
		if os.path.exists(subdirpath):
			for file in os.listdir(subdirpath):
				if file.endswith(".json"):
					copyfile(file, "/home/pi/locations")
					break;
				else:
					print("file not found")
		else:
			print("path not found")
				
	