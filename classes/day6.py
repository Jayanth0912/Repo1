ls = ["pradeep","vinay","baba","kiran"]
# List Comprehension
# final_ls = []
# for each in ls:
#     final_ls.append(each.capitalize())
# print(final_ls)
#
# print([each.capitalize() for each in ls])

# Dict Comprehension
final_dc = {}
counter = 0
for each in ls:
    final_dc[each] = counter
    counter += 1
print(final_dc)

#---------------------------------------
# final_dc2 = {}
# for index,each in enumerate(ls):
#     final_dc2[each] = index
# print(final_dc2)
#
# print({each.capitalize():ind for ind,each in enumerate(ls)})
#-----------------------------------------------------
# Files
#OS Module
# f = ""
# import os


# print(os.listdir())
# print(os.remove("samp.py"))
# print(os.listdir())
# os.rename("currency.py","currency_edit.py")
# os.rmdir("python_dir")

# f1 = open("file_edit.txt","w")
# for each in f1:
#     print(each)
# f1.seek(1)
# print(f1.name)
# print(f1.mode)
# print(f1.write("Hello all welcome to the class"))
# f1.close()
#
# with open("file_edit.txt","a") as f1:
#     f1.write("\nThis is written inside new file opening")
#
#
# with open("file_edit.txt","r") as f1:
#     for each in f1:
#         if "Hello" in each:
#             print("Hello is available in file")

# import datetime
#
# print(datetime.datetime.now())


# Compiler vs Interpreter - Cython,Jython
# Variables, Data types, Conversions
# Control Statements
# Functions
# Files, comprehension

# create a log file
# Write Time to it every 2 min once for 10min

