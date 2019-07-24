"""
Homework Assignment #10: Importing

"""
import os

#list of functions under o
print(dir(os))

# get current working directory
cur_dir = os.getcwd()
print('Current Working directory: ',cur_dir)

# to print files and directories in the current directory
print('Listing files and directories:\n', os.listdir() )

#change working directory
os.chdir("data")
print("Listing again the files and directories: ", os.listdir())

#back to main
os.chdir("../")

#create a directory
os.mkdir("sub1")

#remove a directory
os.rmdir("sub1")

#create nested directories
os.makedirs("sub1/sub2")

#remove nested directories
os.removedirs("sub1/sub2")

#create a file
with open(os.path.join(cur_dir, "sample.txt"), "w"):
    pass

# rename an existing file
try:
    filename = "sample.txt"
    os.rename("sample.txt", "test.txt")
except:
    print("No such file exists.")

#check if the path exists
print("Path exists: ", os.path.exists("test.txt"))

#check if the path is directory
print("Path exists and is a directory: ",os.path.isdir("test.txt"))

#check if the path is a file
print("Path exists and is file: ",os.path.isfile("test.txt"))

# split a path
path = os.getcwd()
filepath = os.path.join(path, "main.py")
(dirname, filename) = os.path.split(filepath)
print("Split directory: ", dirname)
print('Split file: ', filename)
(filename, extension) = os.path.splitext("main.py")
print("Split filename: ",filename)
print("Extension: ",extension)

#stats
print('File stats: ',os.stat("test.txt"))

#remove a file
try:
    filename = "test.txt"
    os.remove(filename)
except OSError:
    print("File can't be removed")