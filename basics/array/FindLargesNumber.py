import array

a = array.array('i', [1,9,5,2,7])
largest = a[0]
l = len(a)
for i in range(1, l):
    if a[i] > largest:
        largest = a[i]
print(largest)