#OOPS
# highlevel object oriented interpreter based programming language

# def add(a,b,c):
#     return a+b+c

# def add(a,b):
#     return a+b
#
# print(add(1,2))


"""
mobile : 
    properties:
        colour
        dimensions
        processor
        camera
        screen
        ram
        storage
    behaviours:
        calls
        using internet
        communication

student :
    properties:
        name:
        age:
        class:
        school:
    behaviours:
        playing_games
        reading_book

"""

"""
classes : A class is a model which contains properties and methods which can used while making an object and using them
objects : Instances of classes
polymorphism : overriding and overloading
encapsulation : Hiding of data
inheritance : the import properties and methods from parent classes to derieved
"""


class Student:

    def __init__(self,name,info,hobbies):
        self.name = name
        self.info = info
        self.hobbies = hobbies

    def get_info(self):
        return self.info

    def get_name(self):
        return self.name

    @staticmethod
    def get_hobbies():
        return ["cricket","chess"]


class Employee:

    def __init__(self,name,info,hobbies):
        self.name = name
        self.info = info
        self.hobbies = hobbies

    def get_info(self):
        return self.info


    def get_name(self):
        return self.name

    @staticmethod
    def get_hobbies():
        return ["news","music"]


# print(Student.get_info())
ram = Student("Ram",{"age":10,"address":"2-2"},["cricket"])
shyam = Student("Shyam",{"age":20,"address":"2-4"},["chess"])
print(ram.get_info())
print(ram.get_name())
print(shyam.get_info())
print(shyam.get_name())
print(Student.get_hobbies())

# jayanth = Employee("Jayanth",{"age":11},["movies"])
#
# print(jayanth.get_name())

#Polymorphism


# def add(ls):
#     return sum(ls)

