#
#
# def add(a,b):
#     c = a+b
#     return c
#
# def sub(a,b):
#     c = a-b
#     return c
#
def mul(a, b):
    c= a*b
    return c


# def div(a,b):
#     c = a/b
#     return c


# a = 10
# b = 5
#
# print(add(a,b))
# print(add(99,1))

# Exceptions

def div(a,b):
    try:
        # if a == 0 or b ==0:
        #     print("can't divide Zero")
        # else:
        print(a / b)
    except Exception as e:
        # Write error into log file
        print("Unable to Perform Division Operation, Please Pass on the valid input!!!")
    finally:
        print("This is finally block")

div(10,0)

# div(10,"a")
# div(10,[])
# div(10,"#")
# fn:                            ln:

