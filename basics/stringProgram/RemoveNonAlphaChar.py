mystr = "Hello, Python!123"
# Approach 1
# char = []
# for x in mystr:
#     if x.isalpha():
#         char.append(x)
# newChar = ''.join(char)
# print(newChar)

# Aproach 2
def remove_non_alpha(mystr):
    result = ''.join([x for x in mystr if x.isalpha()])
    return result