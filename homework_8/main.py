"""
Homework Assignment #8: Input and Output (I/O)

"""

import os

def startNoteTaking():
    print('Starting to take note.')
    askFilename()

#it asks the user the file name
def askFilename():
    file_name = input("Please enter the file name:\n")
    file_path = "./" + file_name + ".txt"
    if fileExists(file_path):
        askFileMode(file_path)
    else:
        askFileInput(file_path)
    

# checks if a file exists or not
def fileExists(file_path):
    if os.path.exists(file_path) and os.path.isfile(file_path):
        return True
    return False

# ask the content to be written to the file
def askFileInput(file_path):
    txt = input('Please write down the content:\n')
    writeToFile(file_path, txt+"\n")
    print('Content written...')


def askFileMode(file_path):
    choice = input('\nWhat do you wish to do? Enter the number against the choice.\n1 read the file\n2 delete the file and start over\n3 append the file\n4 replace a single line\n\n')
    if choice == "1":
        txt = readFile(file_path)
        print('*****YOUR FILE******')
        print(txt)
        print('***********')
    elif choice == "2":
        deleteFile(file_path)
        createEmptyFile(file_path)
        print('File is deleted and empty one is made.')
    elif choice == "3":
        txt = input("Please enter the content, you wish to add:\n\n")
        appendToFile(file_path, txt)
        print('Content added!')
    elif choice == "4":
        updateLineInFile(file_path)
    else:
        print('Sorry, this is not an acceptable option!')

def updateLineInFile(file_path):
    line_counter = 1
    line_array = []
    with open(file_path, "r") as file:
        for line in file:
            print(line_counter , " " , line)
            line_counter += 1
            line_array.append(line)
    line_num = input('\nEnter the line number you wish to replace:\n')
    line_num = int(line_num)
    if line_num <= len(line_array):
        txt = input('Enter the new line:\n')
        line_array[line_num - 1] = txt   
        paragraph = ("\n").join(line_array)
        writeToFile(file_path, paragraph)
        print('\nFile content replaced!')
    else:
        print('Sorry, invalid line number.')
        

# utility function to write certain content to a file
def writeToFile(file_path, content):
    file = open(file_path, "w")
    file.write(content)
    file.close()


#utility function to read content from a file
def readFile(file_path):
    content = ""
    with open(file_path, "r") as file:
        for line in file:
            content = content + line
    return content

# append to an existing file
def appendToFile(file_path, txt):
    file = open(file_path, "a")
    file.write(txt)
    file.close()

# delete a file
def deleteFile(file_path):
    os.remove(file_path)

# create an empty file
def createEmptyFile(file_path):
    file = open(file_path, "w")
    file.close()


startNoteTaking()