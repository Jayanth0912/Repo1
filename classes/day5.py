# a =.1
# b =.1
# c =.1
# print(a+b == 0.2)
# print(a+b+c == 0.3) # True or False?
# print(a+b+c)
# x = 0.1508567
# y = 0.158765
# z = 0.154464
#
# p = round(a+b+c,2)
# print(p==0.3)                 `

# 1/3 = 0.3333333333333333333333333334


# Functions
# Function Definition - body of the function
# Function Declaration - representation of availability
# Function call - usage point of the function



def greetings_to_class():
    print("Hello Team, Welcome to Class")

def greetings_to_individual(student):
    print("Hello",student,"Welcome to the class")


def add(a,b):
    # print(a+b)
    return a+b

def swap_two_nums(a,b):
    a,b = b,a
    return a,b

#call a function to execute the actual statements of the function
# greetings_to_class()
# greetings_to_individual("Anand")
# greetings_to_individual(["Anand","Kiran"])
# add(100,30)
x = 120
# print("----------------->",type(add(100,30)))
# print(add(100,30))
# print("----------------->",type(x))
if add(100,30) > x:
    print("Addition is holding a bigger value")

a = 10
b = 20
print(a,b)
a,b = swap_two_nums(a,b)

print(a,b)
from test_fun import calculate_diff
print(calculate_diff(10,20))
print(calculate_diff(100,20))




# ls = ["Anand","Kiran"]
#
# print(", ".join(ls))
# greetings_to_individual(", ".join(ls))


# create a QR using python to share a file/resume

