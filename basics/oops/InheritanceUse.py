class Parent:
    parentAttr = 100

    def __init__(self):
        print("Calling parent constructor")

    def parentMethod(self):
        print("This is parent method")

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("Parent attr:" , Parent.parentAttr)


class Child(Parent):

    def __init__(self):
        print("Calling child constructor")

    def childMethod(self):
        print("This is child method")


c = Child()
c.parentMethod()
c.setAttr(300)
c.childMethod()
c.getAttr()
