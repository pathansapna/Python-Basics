list_tuples = [("name" ,"Alice"),("one", 1), ("two", 2)]
# d2 = dict(list_tuples)
# print(d2)
d2 = {}
for k,v in list_tuples:
    d = { k : v}
    d2.update(d)
print(d2)    