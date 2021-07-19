import os
import DocSettings
import DocMaker

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

userInput = input("Type /s keyword to search for all files containing that keyword:\n")
if userInput[:2] == "/s":
    choices = search(userInput[3:])
    if choices is None:
        print("Files not found")
    else:
        printChoices(choices)
else:
    print("Not a valid command")       
