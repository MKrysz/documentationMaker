import os
from types import FunctionType
from typing import List
import DocSettings
import DocMaker

commands = {
    "s": "/s keyword to search for all files containg that keyword",
    "x": "/x to exit",
    "r": "/r new name.x to rename file to 'new name.x'"
}
    
class command:
    id: str #single letter id
    desc: str #one line description
    scope: str #where can this command be used: 'a'- All, everywhere; 'm' - Main menu; 's' - afterSearch
    function: FunctionType

    def __init__(self, id: str, desc: str, scope: str, function) -> None:
        self.id = id
        self.desc = desc
        self.scope = scope
        self.function = function

    def execute(filePath: str, args: str = None):
        return function(filePath, args)

#TODO write graph search
def search(filePath, keyword):
    pass

#TODO rewrite using os functionality
def rename(filePath, newName):
    pass

#TODO rewrite using os functionality
def changeDesc(filePath, newDesc):
    pass

def makeDocs():
    DocMaker.main()

#FIXME
def delete():
    pass

#all commands listed
commands = (
    command('s', "keyword to search for all files containg that keyword", 'a', search),
    command('r', "new name.x to rename file to 'new name.x'", 's', rename),
    command('c', "new description to change the description to 'new description'", 's', changeDesc),
    command('d', "to delete this entry", 's', delete),
    command('m', "to make/remake all documentations", 'm', makeDocs)
)

#gets all commands in given scope
def getCommandsByScope(scope: str) -> List[command]:
    return [cmd for cmd in commands if cmd.scope == scope]

#looks for files with keyword in their name
def search(keyword):
    result = []
    for setting in DocSettings.settings:
        if not setting:
            continue
        for root, dir, files in os.walk(setting[2]):
            for file in files:
                if keyword.lower() in file.lower():
                    result.append(DocMaker.getAddress(root, file))
    return result if result else None

#prints choices with their indexes to the console
def printChoices(choices = []):
    i = 0
    for choice in choices:
        print('[', i, '] ', choice)
        i += 1

#splits users input to command indentifier and command argument
def splitCommand(strCommand):
    return strCommand[:2], strCommand[3:]

def getCommand():
    userInput = input(menuStr)
    return splitCommand(userInput)

def getAction():
    userInput = input(actionStr)
    return splitCommand(userInput)

#gets path to folder of the file specified in path variable
def getPath(path):
    return path[:path.rfind('\\')]

#gets file's name from its path
def getFileName(path):
    return path[path.rfind('\\')+1:]

#renames file both in os and .description
def rename(filePath, newFileName):
    root = getPath(filePath)
    oldFileName = getFileName(filePath)
    os.rename(filePath, DocMaker.getAddress(root, newFileName))
    pathToDescription = DocMaker.getAddress(root, '.description')
    description = open(pathToDescription, "r")
    descriptionLines = description.readlines()
    description.close()
    description = open(pathToDescription, "w")
    for line in descriptionLines:
        if oldFileName in line:
            line = line.replace(oldFileName, newFileName)
        description.write(line)
    description.close()

#changes desription of the file
def changeDescription(filePath, newDescription):
    root = getPath(filePath)
    fileName = getFileName(filePath)
    pathToDescription = DocMaker.getAddress(root, '.description')
    description = open(pathToDescription, "r")
    descriptionLines = description.readlines()
    description.close()
    description = open(pathToDescription, "w")
    for line in descriptionLines:
        if fileName in line:
            line = fileName + " " + newDescription
        description.write(line)
    description.close()

def execute(cmd):
    if cmd[0] == "/s":#if command is search
        choices = search(cmd[1])
        if choices is None:
            print("No files found")
        else:
            #for choosing exact file
            printChoices(choices)
            userInput = input()
            while not userInput.isdigit():
                userInput = input()
            userInput = int(userInput)
            choice = choices[userInput]
            print("You've chosen : ", choice)

            action = getAction()#action is 2-element touple, [0] is function ID, [1] is its argument
            #TODO I recommend adding possible actions' IDs to a touple
            if action[0] == "/r":
                rename(choice, action[1])
            elif action[0] == "/d":
                changeDescription(choice, action[1])
            else:
                print("Invalid command")
    else:
        print("Invalid command")

def main():
    command = getCommand()#command is 2-element touple, [0] is function ID, [1] is its argument
    while command[0] != "/x":
        execute(command)          
        command = getCommand()
    print("Exitting...")
    DocMaker.main()#update .html file

if __name__ == "__main__":
    main()
