#Decorators
# Decorators are the components which are wrapped to any functions to extend its functionality


# def login_required(fun):
#     def inner(name,login_status):
#         if not login_status:
#             print("Kindly Login")
#             return
#         return fun(name,login_status)
#     return inner
#
#
# @login_required
# def home(name,login_status):
#     print("Welcome to Home Page")
#
# @login_required
# def profile(name,login_status):
#     print("Welcome to Home Page")
#
# @login_required
# def settings(name,login_status):
#     print("Welcome to Home Page")
#
# home("Vinay",True)



# eu=3
#
# print(eu *10 + 10 + 30 * 10)

# def parent_fun(msg):
#     def inner():
#         print(msg)
#     inner()
#
#
# parent_fun("Hello My Name is Vinay")


"""
1.
Write a program to count vowels and consonents and print the count in your name
input = "vinay"
output:
vowels: 2
consonents: 3

"""

# ovels = "aeiou"
#
# inp = "vinay"
# ovel_count = 0
# cons_count = 0
# for each in inp:
#     if each in ovels:
#         ovel_count += 1
#     else:
#         cons_count += 1
#
# print(ovel_count)
# print(cons_count)

"""
ls1 = [9,5,2,4,8]

sort the elements in the list in desending order
"""

# ls1 = [9,5,2,4,8]
# ls1.sort()
# print(ls1)
# ls1.sort(reverse=True)
# print(ls1)

"""
ls1 = [9,5,2,4,8] ls2 = [90,30,1,7,40]

merge two lists and sort the elements in the list in ascending order

"""


# ls1,ls2 = [9,5,2,4,8],[90,30,1,7,40]
#
# ls3 = (ls1+ls2)
# ls3.sort()
# print(ls3)

#requests
#json
#os
#sys
#math