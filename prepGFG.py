import re
import pyperclip

OUT = open('OUT.txt','r+') 

with open("IN.txt", "r") as IN:
    data = IN.readlines()
    for line in data:
        x = re.search("^(\s)*/+.*",line)
        if x == None :
            print(line.rstrip())
            OUT.write(line.rstrip()+"\n")

OUT.seek(0,0)
pyperclip.copy(OUT.read())

OUT.close()
