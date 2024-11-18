from curses.ascii import isalpha

d1 = {
    "name" : "Alice",
    "age" : 24,
    "city" : "Paris"
}
d2 = {}
#Approach 1

# for k, v in d1.items():
#     if not str(v).isdigit():
#         d = {k: v}
#         d2.update(d)
# print(d2)

for k, v in d1.items():
    if not isinstance(v, (int, float)):
        d = {k: v}
        d2.update(d)
print(d2)