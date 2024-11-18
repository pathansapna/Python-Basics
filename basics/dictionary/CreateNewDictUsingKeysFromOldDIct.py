d1 = {
    "name": "ALice",
    "age" : 24,
    "city" : "Nagar"
}
keys = ["name", "age"]
d2 = {}
for key in keys:
    d2[key] = d1[key]
print(d2)