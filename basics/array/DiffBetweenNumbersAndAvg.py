#Python program find difference between each number in the array and the average of all numbers
import array

a= array.array('i', [2,4,6,8])
avg = sum(a) / len(a)
for i in range(len(a)):
    diff = avg - a[i]
    print(diff)