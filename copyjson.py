import glob, os
from shutil import copy

def copyjson():
        for subdir in os.listdir("/media/pi/"):
                print(subdir)

                subdirpath = "/media/pi/"+subdir

                if os.path.exists(subdirpath):
                        for file in os.listdir(subdirpath):
                                print(file)
                                if file.endswith(".json"):
                                        print("hi")
                                        copy(subdirpath+"/"+file, "/home/pi/locations")
                                        print("bye")
                                        break;
                                else:
                                        print("file not found")
                else:
                        print("path not found")
                                
        
