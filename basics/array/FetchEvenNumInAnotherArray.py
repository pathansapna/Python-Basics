import array

a = array.array('i', [2,4,3,5,6,7,9])
b = array.array('i',)
l = len(a)
for i in range(l):
    if a[i]%2==0:
        b.append(a[i])
print(b)