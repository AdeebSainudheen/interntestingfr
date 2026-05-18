class Person:
    def __init__(self,name):
        self.name = name

    def greet(self):
        print("Hello, " + self.name + "!")

p1 = Person("Alice")
p1.greet()