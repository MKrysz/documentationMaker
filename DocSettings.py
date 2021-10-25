comp = 'Bartek'

#provide path and name of created .html file, title of page, path to your documentation
if comp == 'Maciek':
    settings = (
        ("C:/Users/macie/Documents/Documentation/documentation.html",#file name
        "Electronic documentation",#web page's title
        "C:/Users/macie/Documents/Documentation"),#directory

        #second set for another .html file
        ("C:/Users/macie/Books/Library.html",
        "Library",
        "C:/Users/macie/Books")
    )
elif comp == 'Bartek':
    settings = (
        ("D:/barte/documentation_manager/documentationMaker/biblioteka.html",#file name
        "biblioteka Bartek",#web page's title
        "D:/barte/biblioteka"),#directory   
        ()
    )

#change extensions you want to include in your web page
readableExtensions = ("pdf", "html", "jpg", "txt", "png")
