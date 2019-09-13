OUT = open('OUT.txt','w') 

with open("IN.txt", "r") as IN:
    data = IN.readlines()
    for line in data:
        print(line)
        OUT.write(line.rstrip()+"\n")

OUT.close()
