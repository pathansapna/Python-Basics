# List of dictionaries
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 9},
    {"name": "Charlie", "age": 8},
]

people_sorted = sorted(people, key= lambda x : x['age'])
for person in people_sorted:
    print(person)
