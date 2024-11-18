class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'My name is {self.name}')


n = Person("Josh")
print(n.name)
n.talk()
