student_information = {
    "name" : "Alice",
    "age" : 21,
    "city" : "Nagar"
}

#Update age
student_information["age"] = 32

#Adding new key:value
student_information["Graduation_year"] = 2003
print("Updated dictionary: ", student_information)

#Remove item using del
del student_information["city"]
print("student_info:", student_information)

#REmove item using pop()
student_information.pop("Graduation_year")
print("Removed graduation year: ", student_information)

#Remove item using popitem
student_information.popitem()
print("Remove last item: ", student_information)