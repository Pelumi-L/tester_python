# class Animal:
#     def __init__(self, name) -> None:
#         self.name = name
#     def fname(self):
#         print(f"the name of my dog is {self}")
#     def speak(self):
#         print(f"my doggie goes {self}")

# dog = Animal
# dog.fname('skipper')
# dog.speak('ruff ruff')
class Person:
    def __init__(self, name, number):
        self.name = name
        self.number = number
    def display(self):
        print(f"my name is {self.name}")

class Employee(Person):
    def __init__(self, name, number, age):
        super().__init__(name, number)
        self.name = name
        self.number = number
        self.age =  age
    def details(self):
        print(f"my name is {self.name}")

# joshua = Person('joshua', 815362516)
# joshua.display()

mgt = Employee('john', 1234, 21)
mgt.display()
#print an person object with name, gender, qualification, occupation. then a child object with firstname and surname(coming from person name), class, describe the child in reference to the parent