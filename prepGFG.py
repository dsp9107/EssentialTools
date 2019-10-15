import re
input_file = 'IN.txt'
with open(input_file,"r") as f:
    data = f.read()
# Remove multi empty lines 
data=re.sub(r'\n\s*\n','\n',data,re.MULTILINE)
# Remove single line comments
data=re.sub(r'\n#.*', "", data)
# Remove multi comments in code
for x in re.findall(r'("[^\n]*"(?!\\))|(//[^\n]*$|/(?!\\)\*[\s\S]*?\*(?!\\)/)',data,8):data=data.replace(x[1],'')

with open("OUT.txt", "w") as f:
    f.write(data)
