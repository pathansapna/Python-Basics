students_info = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science"
}

#Creating dictionary using dict()
new_dict = dict(name = "Sapna", age = "33")
print(new_dict)
#Access item using key
name = students_info["name"]

#Accessing item using get() method
age = students_info.get("age")
print(age)
print(name)
