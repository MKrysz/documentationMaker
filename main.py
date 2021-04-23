import os
import webbrowser

# change name of created html file and directory to your documentation
htmlName = "documentation.html"
dir = "C:/Users/macie/Documents/Documentation"


# creates .html file and writes basic html template
def startFile():
    file = open(htmlName, 'w')
    file.write("<!DOCTYPE html>\n")
    file.write("<html>\n")
    file.write("<head>\n")
    file.write("<title>Electronic documentation</title>\n")
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
    buffer = "<li><a href=\"" + getAddress(directory, doc) + "\" target = \"_blank\">" + doc[:-4]
    file.write(buffer + "</a></li>\n")

def getAddress(directory, doc):
    result = directory + '/' + doc
    if os.name == "nt":
        result = result.replace('/', '\\')
    return result

def addDescripion(txtFile):
    file.write(str(txtFile.read()))
    file.write("<p></p>\n")

#main recursive function
def rek(dir):
    result = list(os.walk(dir))[0]
    if result[1]:
        for subDir in result[1]:
            startList(subDir)
            rek(dir + '/' + subDir)
            closeList()
    else:
        if not result[2]:
            addItem(result[0], "empty.pdf")
        for doc in result[2]:
            if doc[-3:] == "pdf":
                addItem(result[0], doc)
                for txtFile in result[2]:
                    if txtFile == doc[:-4] + ".txt":
                        description = open(getAddress(result[0], txtFile), 'r')
                        addDescripion(description)


gen = list(os.walk(dir))
file = startFile()
rek(dir)
closeFile()
webbrowser.open_new_tab(htmlName)
