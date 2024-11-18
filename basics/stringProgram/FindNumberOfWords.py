mystr = "Python program to find number of words in a string"

#  Approach 1:
# count = 0
# word = False
# for char in mystr:
#     if char != ' ':
#         if not word:
#             count += 1
#             word = True
#     else:
#         word = False
#
# print(count)

# Approach 2
word = mystr.split()
print(len(word))