import os
import DocSettings
import DocMaker

menuStr = "Type :\n"\
"/s keyword to search for all files containg that keyword\n"\
"/x to exit\n"



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

def Command(strCommand):
    return strCommand[:2], strCommand[3:]

def getCommand():
    userInput = input(menuStr)
    return Command(userInput)

def execute(cmd):
    if cmd[0] == "/s":
        choices = search(cmd[1])
        if choices is None:
            print("No files found")
        else:
            printChoices(choices)
    else:
        print("Invalid command")

command = getCommand()
while command[0] != "/x":
    execute(command)          
    command = getCommand()
print("Exitting...")