import os
import DocSettings


# creates .html file and writes basic html template
def startFile(HTMLname, WebTitle):
    file = open(HTMLname, 'w')
    file.write("<!DOCTYPE html>\n")
    file.write("<html>\n")
    file.write("<head>\n")
    file.write("<title>" + WebTitle + "</title>\n")
    file.write("</head>\n")
    file.write("<body>\n")
    file.write("<ul>\n")
    return file


# writes basic template and closes .html file
def closeFile():
    file.write("</ul>\n")
    file.write("</body>\n")
    file.write("</html>\n")

#starts html list with 'name' header
def startList(name):
    file.write("<p></p> <li><ul><h><b>" + name + "</b></h>\n")

#closes list
def closeList():
    file.write("</ul></li>\n")

#adds pdf file to a list
def addItem(directory, doc):
    buffer = "<li><a style=\"color:blue\" href=\"" + getAddress(directory, doc) + "\" target = \"_blank\">" + doc
    file.write(buffer + "</a></li>\n")

def getAddress(directory, doc):
    result = directory + '/' + doc
    if os.name == "nt":
        result = result.replace('/', '\\')
    return result

def addDescripion(descLines, doc):
    for line in descLines:
        index = line.find(doc)
        if index > -1:
            file.write(line[index + len(doc):] + "<p></p>")
            return 1
    return 0


#main recursive function
def main(directory):
    result = list(os.walk(directory))[0]
    if result[1]:
        for subDir in result[1]:
            startList(subDir)
            main(directory + '/' + subDir)
            closeList()
    else:
        description = 0
        descriptionFound = 0
        for doc in result[2]:
            if doc == ".description":
                descriptionFound = 1
                descriptionFile = open(getAddress(result[0], doc), 'r+')
                description = descriptionFile.readlines()
                break
        if not descriptionFound:
            descriptionFile = open(getAddress(result[0], ".description"), 'w')
            description = ("none", "none")
        for doc in result[2]:
            extension = doc[doc.find('.')+1:]
            if extension in DocSettings.readableExtensions:
                if doc == ".description":
                    continue
                addItem(result[0], doc)
                if description:
                    if not addDescripion(description, doc):
                        buffer = input("add description for " + doc + '\n')
                        descriptionFile.write('\n' + doc + ' ' + buffer)
                        file.write(buffer + "<p></p>")
        descriptionFile.close()


#run main for every setting
for setting in DocSettings.settings:
    file = startFile(setting[0], setting[1])
    main(setting[2])
    closeFile()


