# # OOPs -> Inheritance
#
#
# class Person:
#     def __init__(self,address,name):
#         self.name = name + " is a Person"
#         self.address = address
#
#     def get_person_details(self):
#         return self.name,self.address
#
#     def get_info(self):
#         return "I am a Person"
#
# class Student:
#     def __init__(self,address,name):
#         self.name = name + " is a Student"
#         self.address = address
#
#     def get_student_details(self):
#         return {self.name:self.address,"type":"student"}
#
#     def get_info(self):
#         return "I am a Student"
# # class Employee(Person):
# #     pass
#
#
# # ajay = Person("Madanapalle","Ajay")
# # print(ajay.get_person_details())
#
# class Employee(Person,Student):
#     # def __init__(self,address,name):
#     #     self.name = name + " is an Employee"
#     #     self.address = address
#     # pass
#     def __init__(self,address,name):
#         super(Person, self).__init__(address,name)
#
# emp = Employee("Andhra","Kiran")
#
# print(emp.name)
# # print(emp.get_person_details())
# # print(emp.get_student_details())
#
# print(emp.get_info())
# print(emp.get_student_details())
#
#
# # Super with same methods and different return
#
#
#
#
#
#
#


# Simple / Single
# Multiple
# Multilevel
# Hierarchical

# # Single/Simple
# class parent:
#     def class_name(self):
#         print("I am a parent")
#
#
# class child(parent):
#     def info(self):
#         print("I am a child")
#
#
# obj = child()
# obj.info()
# obj.class_name()


# # Multiple
# class parent1:
#     def class_name(self):
#         print("I am a parent1")
#
# class parent2:
#     def get_class_name(self):
#         print("I am parent2")
#
# class child(parent1,parent2):
#     def info(self):
#         print("I am a child")
#
#
# obj = child()
# obj.info()
# obj.class_name()
# obj.get_class_name()


# # Multi Level
# class parent1:
#     def class_name(self):
#         print("I am a parent1")
#
# class parent2(parent1):
#     def get_class_name(self):
#         print("I am parent2")
#
# class child(parent2):
#     def info(self):
#         print("I am a child")
#
#
# obj = child()
# obj.info()
# obj.class_name()
# obj.get_class_name()

# # Multiple
# class parent1:
#     def class_name(self):
#         print("I am a parent1")
#
# class parent2(parent1):
#     def get_class_name(self):
#         print("I am parent2")
#
# class child(parent1):
#     def info(self):
#         print("I am a child")
#
#
# obj = child()
# obj.info()
# obj.class_name()
# obj2= parent2()
# obj2.get_class_name()


# class parent:
#     def __init__(self,fname,lname):
#         self.fn = fname
#         self.ln = lname
#     def info(self):
#         print(self.fn,self.ln)
#
# class child(parent):
#     def __init__(self,fname,lname):
#         parent.__init__(self,fname,lname)
#         self.age = 20
#
#     def info(self):
#         print(self.fn,self.ln,self.age)
#
#
# obj = child("vinay","jai")
# obj.info()


# Decorators
# Python Practise

# Git
# Rest APIS
# Selenium



# login()

# home()
# dashboard()
# profile()
# fun14()
# fun15()


# def check_login():
#     pass
#
# @check_login
# def home():
#     pass

"""
1.
Write a program to count vowels and consonents and print the count in your name
input = "vinay"
output:
vowels: 2
consonents: 3

2.
ls1 = [9,5,2,4,8]

sort the elements in the list in desending order

3.
ls1 = [9,5,2,4,8] ls2 = [90,30,1,7,40]

merge two lists and sort the elements in the list in ascending order



"""









