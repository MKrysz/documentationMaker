import os

def greeterPrint():
    print("Welcome to documentation Editer")
    print("Write \'exit\' to exit")
    print("Write f filePath to load pdf file in order to perform operations")

def loadFilePrint(fileName):
    print(fileName, "loaded")
    print("type \'desc newDescription\' to change description")
    print("\'rename newName\' to rename")
    print("\'copy copysName copysPath\' to copy the file, not setting the path will paste in current dir")

