# # Keywords
# """
# if
# else
# print
# while
# and
# is
# or
# for
# def
# class
# list
# """
# print("Hello")
# print("Welcome")
# x = 10
# #
# # ls = [1,2,3]
# # lis = list([1,2,3])
# # list = "456789"
# #
# # ls1 = list([1,2,2,3,4])
# if x == 10:
#     print("x is 10")
#
# """
# Data Types and Conversions
# Str
# Numerical
# List
# Dict
# Set
# tuple
#
# Conversions
# str - num
# num - str
# list - set
# set - list
# tuple - list
#
# """

def login_required(f1):
    def inner(name,is_login):
        if is_login == False:
            print("Kindly Login")
            return
        return f1(name,is_login)
    return inner

@login_required
def home(name,is_login):
    print("Welcome to Dashboard")

home("user",False)