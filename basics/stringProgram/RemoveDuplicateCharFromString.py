mystr = 'Hello, Python!'
char = []
for x in mystr.lower():
    if x not in char:
        char.append(x)

NewChar = ''.join(char)
print(NewChar)