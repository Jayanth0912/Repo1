# control statements
# conditional statements
# Looping statements
# jumping statements


# conditional statements
# if,elif,else


# if <expression>:
#     statements

# p1_age = 70
#
# if p1_age >= 18:
#     print("P1 is a major")
# if p1_age >= 18 and p1_age <= 60:
#     print("Person is a middle age candidate")
# if p1_age <=18 or p1_age >= 60:
#     print("ticket cost is reduced to half")
# if p1_age >= 60:
#     print("P1 is a oldage person")
# if p1_age >= 18:
#     if p1_age < 60:
#         print("p1 id=s a middle age guy")
#     if p1_age >= 60:
#         print("P1 is a oldage person")
#
#
# if p1_age >= 18 and p1_age <= 60:
#     print("Person is a middle age candidate")
# else:
#     print("person is a child or oldage candidate")

"""
if x == 10:
    print("x is 10")
if x != 10:
    print("x is not 10")
if cond:
    statement 1
if not cond:
    statement x
-----------------
if cond:
    statement 1
else:
    statement x
"""
# x = 10
# if x == 10:
#     print("x is 10")
# if x != 10:
#     print("x is not 10")

# x = 13
#
# if int(str(x)[-1]) % 2 == 0:
#     print("x is divisible by 2")
# elif int(str(x)[-1]) == 0 or int(str(x)[-1]) == 5:
#     print("x is divisible by 5")
# else:
#     print("x is not divisible by 2 or 5")


# looping statements

# for and while
ls = [10,20,30,2,3,4,5]

# for each_ele in ls:
#     if each_ele % 2 == 0:
#         print(each_ele)
#
# for i in range(10):
#     print(i+1,"vinay")

# i = 0
# while i<10:
#     print(i,"My name is vinay")
#     i = i+1


# Break, continue and pass

# i = 0
# while i<10:
#     print(i,"My name is vinay")
#     if i == 5:
#         break
#     i +=1
#
# for i in range(10):
#     print(i,"My name is jayanth")
#     if i==5:
#         break
#     print("34567890")


# if i==0:
#     pass
# else:
#     i = i * 10
i=0
while i <= 10:
    print(i)
    i = i + 1
    if i == 5:
        continue
    print("3456789")

# x = [1,2,3]
# y = [1,2,3]
# print(id(x))
# print(id(y))
# if x == y:
#     print("x is equal to y")
# if x is y:
#     print("x and y are same obj reference")


# Functions
# comprehensions

