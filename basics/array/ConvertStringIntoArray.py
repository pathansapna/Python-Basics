import array

s = "Sapna"
l = list(s)
l2 = []
a= array.array('u', l2)

for i in l:
    a.append(i)
print(a)
# a = array.array('i')
