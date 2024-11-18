# Lambda - is a keyword used to create anonymous functions(without a name function)

#Square elements
# original_list = [1,2,3,4,5]
# squared_list = [(lambda x: x ** 2)(x) for x in original_list]

#OR

# squared_list = [x*x for x in range(1,11)]
# print(squared_list)

#Nested FOr loops
# list1= [1,2,3]
# list2 = [4,5,6]
# result = [(x,y) for x in list1 for y in list2]
# print(result)
#
# #Conditions in List comprehensions
# generate_even = [x for x in range(1, 21) if x%2 == 0]
# print(generate_even)

#With for loop
#Put all non-vowel letters in a list from string
# vowel_list = [x for x in "Hello, Python" if x not in "aeiou"]
# print(vowel_list)

def myfunction(x):
   return x%10
list1 = [17, 23, 46, 51, 90]
print ("list before sort", list1)
list1.sort(key=myfunction)
print ("list after sort : ", list1)