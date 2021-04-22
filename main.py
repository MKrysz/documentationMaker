import os

def startFile():
    file = open('documentation.html', 'w')
    file.write("<!DOCTYPE html>\n")
    file.write("<html>\n")
    file.write("<head>\n")
    file.write("<title>Electronic documentation</title>\n")
    file.write("</head>\n")
    file.write("<body>\n")
    file.write("")
    return file

def closeFile():
    file.write("</body>\n")
    file.write("</html>\n")

def startList(name):
    file.write("<li><ul><b>" + name + '</b>\n')

def closeList():
    file.write("</ul></li>\n")

def addItem(directory, doc):
    buffer = "<li><a href=\"" + directory + '/' + doc + "\" target = \"_blank\">"+ doc[:-4]
    if isWindows:
        buffer = buffer.replace('/', '\\')
    file.write(buffer + "</a></li>\n")


dir = "C:/Users/macie/Documents/Documentation"
gen = list(os.walk(dir))
isWindows = 1

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

file = startFile()
rek(dir)
closeFile()
