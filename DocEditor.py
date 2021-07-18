import os
import DocSettings

print("Choose path to file or type /s 'keyword' to search for all files containing that keyword:")
i = 0
for setting in DocSettings.settings:
    print('[', i, '] ', setting[2])
    i += 1
userInput = input()
if userInput.isdigit:
    choice = int(userInput)
    result = DocSettings.settings[choice][2]
result = list(os.walk(result))[0][1]
print(result)