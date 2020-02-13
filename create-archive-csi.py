import shutil
import os
import sys
import gnupg

try:
    dir_name = sys.argv[1]
except IndexError:
    dir_name = input("Please enter name of folder that needs to be submitted: ")

source = os.getcwd() + "/"  + dir_name + ".zip"
destination = os.getcwd() + "/" + dir_name + "/dist/" + dir_name + ".zip"
root_of_dist = os.getcwd() + "/" + dir_name + "/dist/"
print(source + " to " + destination)
print("Zipping Folder...")
shutil.make_archive(dir_name, 'zip', dir_name)
print("Folder zipped!")
if not os.path.exists(os.getcwd() + "/" + dir_name + "/dist/"):
    os.mkdir(os.getcwd() + "/" + dir_name + "/dist/")
shutil.move(source, destination)