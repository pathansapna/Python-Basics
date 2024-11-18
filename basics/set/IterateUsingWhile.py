my_set = {1,2,4,2,5}

#COnverting set to an iterator
set_iter = iter(my_set)

#looping through each item in the set using a while loop
while True:
    try:
        #Getting the next item from the iterator
        item = next(set_iter)

        #Performing operations on each element
        print("Item: ", item)
    except StopIteration:
        #If StopIteration is raised, break from the loop
        break