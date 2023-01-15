
# Exercise 2 : Person class and child Student class
# UC1. Create a Python class Person with attributes: name and age of type string.
# UC2. Create a display() method that displays the name and age of an object created via the Person class.
# UC3. Create a child class Student  which inherits from the Person class and which also has a section attribute.
# UC4. Create a method displayStudent() that displays the name, age and section of an object created via the Student class.
# UC5. Create a student object via an instantiation on the Student class and then test the displayStudent method.


# UC 1. Person class with attributes: name and age of type string.
class Person:

    # attributes
    name = ""
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # UC 2. display() method that displays the name and age of an object created via the Person class.
    def display(self):
        print("Person name : ", self.name)
        print("Person age : ", self.age)

# initialized the attributes values
person = Person("Bridgelabz",27)

# Calling the display() method from Person class
person.display()