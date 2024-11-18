mystr = 'He12llo, Py00th55on!'
digits = [str(x) for x in range(10)]
chars = []
for x in mystr:
    if x not in digits:
        chars.append(x)
newstr = ''.join(chars)
print(newstr)
