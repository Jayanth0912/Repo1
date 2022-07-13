#lambda
#modules
#operator overloading
#variable ops
#string formats
#OOPS


# Lambda functions

# def cal_square(n):
#     return n**2
#
# print(cal_square(5))
# Headless Functions
# x = lambda n : n ** 2
# y = lambda a,b,c,d : a ** 2+b**3 + c -d
# print(x(5))
# print(y(1,2,3,4))

#Modules

import class_tutorial
import platform
import os
print(class_tutorial.my_name)
print(class_tutorial.my_address)
print(class_tutorial.f1())
print(class_tutorial.f2(class_tutorial.my_name))


"""
+
-
*
/
%
"""

# x = 10
# y = 20
#
# print(x+y)
#
# a = "jayanth"
# b = "vinay"
#
# print(a+b)
#
# ls1 = [1,2,3]
# ls2 = [4,5,6]
#
# print(ls1+ls2)
# ls1.append(ls2)
# print(ls1)
#
# print(a*x)
# print(x*a)


# a = 10
# b = 20
# a,b,c = "10",20,30

# a = b = 10
#
# def f1(a,b,c):
#     return a-b,b-a,c-b
#
#
# x,y,z = f1(10,5,20)

# print(x,y,z)

# swap two numbers
# a = 10
# b = 20
#
# print(a,b)
#
# c = a
# a = b
# b = c
#
# a,b = b,a
# print(a,b)



#string formats
def greet(name,class_name,topic):
    # print("Hello",name,"Welcome to",class_name,"on",topic)
    # print("Hello "+name+" Welcome to "+class_name+" on "+topic)
    print("Hello {} Welcome to {} on {}".format(name,class_name,topic))
    print("Hello {name} Welcome to {cls_name} on {topic_name}".format(name=name,cls_name=class_name,topic_name=topic))
    # print("Hello {}".format(name))

greet("kiran","Demo Class","Python")
# greet("ajay") 




