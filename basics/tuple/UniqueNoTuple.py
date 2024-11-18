#Python program to find unique numbers in a given tuple −

my_tuple = (2,1,3,2,4,2,3,4,5,6)
# list = list(my_tuple)
# new_list = []
#
# for x in my_tuple:
#     if x not in new_list:
#         new_list.append(x)
#
# print(new_list)
# print("New - ", tuple(new_list))
#

#Aproach 2
T2 = ()
for x in my_tuple:
   if x not in T2:
      T2+=(x,)
print ("original tuple:", my_tuple)
print ("Unique numbers:", T2)