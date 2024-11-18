class Parent:
    def myMethod(self):
        print("Calling parent method")


class Child(Parent):
    def myMethod(self):
        print("Calling child method")


#Instance of Child class
c = Child()
#overridding parent method and calling child method
c.myMethod()