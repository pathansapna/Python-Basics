stud_info = {
    "name" : "Alice",
    "age" : 24,
    "city" : "Nagar"
}
#Using keys
for key in stud_info:
    print("Keys: ", key, stud_info[key])

#Using values
for value in stud_info.values():
    print("Values: ", value)

#Using items()
for key, value in stud_info.items():
    print("Items: ", key, value)