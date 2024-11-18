import array

a = array.array('i', [3,4,6,7,8])
avg = 0
# sum = 0
# for i in range(len(a)):
#     sum += a[i]
#     avg = sum / len(a)
# print(avg)

b = sum(a) / len(a)
print(b)

