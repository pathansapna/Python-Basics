class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(5,4)
v2 = Vector(3.6, -2)
print(v1 + v2)


############################################################################
#Another programm of Overloading concept
class OverloadExample:

    def display(self, *args):
        if len(args) == 1:
            print(f"Argument: {args[0]}")
        elif len(args) == 2:
            print(f"Arguments: {args[0]}, {args[1]}")
        else:
            print("Invalid number of arguments")

# Create object
obj = OverloadExample()

obj.display(5)           # Calls method with 1 argument
obj.display(5, 10)       # Calls method with 2 arguments
obj.display(3.14, 7)     # Calls method with 2 arguments