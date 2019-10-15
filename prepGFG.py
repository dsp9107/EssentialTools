import re
import pyperclip

OUT = open('OUT.txt','r+') 
comment = 0
with open("IN.txt", "r") as IN:
    data = IN.readlines()
    for line in data:
        x = re.search("^(\s)*/+.*",line)
        start = re.search("(/\*)+",line)
        end = re.search("[*/]$",line)
        if(end != None and start != None ):
            comment = 0
        elif(end == None and start == None and comment == 1):
            comment = 1
        elif(start != None):
            comment = 1
        elif(end != None and comment ==1):
            comment =0
        elif x == None and start == None and end==None:
            print(line.rstrip())
            OUT.write(line.rstrip()+"\n")
    
OUT.seek(0,0)
pyperclip.copy(OUT.read())

OUT.close()

