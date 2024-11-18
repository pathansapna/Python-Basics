# Python program to split an array in two and store even numbers in one array and odd numbers in the other.
import array

a = array.array('i', [2,4,5,7,8])
b= array.array('i')
c= array.array('i')

for i in range(len(a)):
    if a[i]%2==0:
        b.append(a[i])
    else:
        c.append(a[i])
print("Even array - ", b)
print("Odd array - ", c)


