d1 = {
    "name" : "Alice",
    "age" : 24,
    "city" : "Paris"
}

d2 = {
    "one" : 1,
    "two": 2
}

merge_dict = {**d1, **d2}
print(merge_dict)