d1 = {"one":"eleven", "2":2, "three":3, "11":"eleven", "four":4, "two":2}

vals = list(d1.values()) #all values
unique_vals = [v for v in vals if vals.count(v) == 1]  #Unique values

d2 = {}
for k, v in d1.items():
    if v in unique_vals:
        d = {k : v}
        d2.update(d)
print(d2)