mystr = 'Hello, Python!'
# Approach 1:
# print (sorted(mystr.lower()))   #using sorted method

# Approach 2(Bubble sort):
def sorting_characters(mystr):
    char_list = list(mystr)   #convert string to list of characters
    n = len(char_list)

    #Bubble sort implementation
    for i in range(n):
        for j in range(0, n-i-1):
            if char_list[j] > char_list[j + 1]:
                char_list[j], char_list[j + 1] = char_list[j + 1], char_list[j]

    return ''.join(char_list)
print(sorting_characters(mystr.lower()))
