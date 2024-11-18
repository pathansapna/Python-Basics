mystr = 'Hello, Python!'
charC = {}

for char in mystr.lower():
    if char in charC:
        charC[char] += 1
    else:
        charC[char] = 1

for char, count in charC.items():
    print(f"'{char} : {count}")

