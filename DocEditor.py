import os
import DocSettings
import DocMaker

#I have to think what the fuck I'm doing here, so TODO whatever the fuck is that
# dct_menu = {
#     "/s" : " keyword to search for all files containg that keyword\n",
#     "/x" : " to exit\n"
# }

# dct_action = {
#     '/r' : "new name.x to rename file to 'new name.x'",
#     '/d' : "new description to change the description to 'new description'\n"
# }

#menu shown on start
menuStr = "Type :\n"\
    "/s" + " keyword to search for all files containg that keyword\n"\
    "/x to exit\n"


#menu shown after choosing a file
actionStr = "Type :\n"\
    "/r new name.x to rename file to 'new name.x'\n"\
    "/d new description to change the description to 'new description'\n"
    #TODO:
    #change /d to /c
    #add /d that deletes specified file and its description
    #add /x that returns to the previous menu


#looks for files with keyword in their name
def search(keyword):
    result = []

    for setting in DocSettings.settings: #for -> walk through tuple in settings (in DocSettings)
        
        for root, dir, files in os.walk(setting[2]): #walk through directories, files and roots
                                            
            for file in files: #it's walk without lookking for directories
                
                if keyword.lower() in file.lower(): #every file
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

            action = getAction()  #action is 2-element touple, [0] is function ID, [1] is its argument
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
    command = getCommand()  #command is 2-element touple, [0] is function ID, [1] is its argument
    while command[0] != "/x":
        execute(command)          
        command = getCommand()

    print("Exitting...")
    DocMaker.main()  #update .html file


#TODO: 
#you know what
main()
