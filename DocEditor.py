import os
import DocSettings
import DocMaker

menuStr = "Type :\n"\
    "/s keyword to search for all files containg that keyword\n"\
    "/x to exit\n"

actionStr = "Type :\n"\
    "/r new name.x to rename file to 'new name.x'\n"\
    "/d new description to change the description to 'new description'\n"



def search(keyword):
    result = []
    for setting in DocSettings.settings:
        for root, dir, files in os.walk(setting[2]):
            for file in files:
                if keyword.lower() in file.lower():
                    result.append(DocMaker.getAddress(root, file))
    return result if result else None

def printChoices(choices = []):
    i = 0
    for choice in choices:
        print('[', i, '] ', choice)
        i += 1

def splitCommand(strCommand):
    return strCommand[:2], strCommand[3:]

def getCommand():
    userInput = input(menuStr)
    return splitCommand(userInput)

def getAction():
    userInput = input(actionStr)
    return splitCommand(userInput)

def rename(pathToOldFile, newFileName):
    return True

def changeDescription(filePath, newDescription):
    return True

def execute(cmd):
    if cmd[0] == "/s":
        choices = search(cmd[1])
        if choices is None:
            print("No files found")
        else:
            printChoices(choices)
            userInput = input()
            while not userInput.isdigit():
                userInput = input()
            choice = choices[userInput]
            print("You've chosen ", choice)
            action = getAction()
            if action[0] == "/r":
                rename(choice, action[1])
            elif action[0] == "/d":
                changeDescription(choice, action[1])
    else:
        print("Invalid command")

#main 
command = getCommand()
while command[0] != "/x":
    execute(command)          
    command = getCommand()
print("Exitting...")