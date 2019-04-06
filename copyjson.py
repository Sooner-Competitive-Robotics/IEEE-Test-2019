import glob, os
from shutil import copy

def copyjson():

        for subdir in os.listdir("/media/"):
                print(subdir)

                subdirpath = "/media/"+subdir+"/"
                print(subdirpath)
                
                if os.path.exists(subdirpath):
                        print("exists")
                        #access = os.access(subdirpath, os.R_OK)
                        #print(access)
                        #if access:
                        #print("before")
                        #print(os.listdir(subdirpath))
                        for file in os.listdir(subdirpath):
                                #print("after")
                                print(file)
                                if file.endswith(".json.txt"):
                                        print("hi")
                                        copy(subdirpath+"/"+file, "/home/pi/locations")
                                        print("bye")
                                        return True
                                else:
                                        print("file not found")
                        else:
                                print("path not acessible")
                else:
                        print("path not found")

        return False
                                
        
