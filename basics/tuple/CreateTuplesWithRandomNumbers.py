# Python program to create a tuple of 5 random integers
import random

my_tuple = ()
for x in range(5):
    x = random.randint(0,100)
    my_tuple += (x, )

print(my_tuple)