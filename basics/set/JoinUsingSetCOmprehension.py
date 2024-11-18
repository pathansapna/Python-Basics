set1 = {1, 2, 3}
set2 = {3, 4, 5}

joined_set = {x for s in [set1, set2] for x in s}
print(joined_set)