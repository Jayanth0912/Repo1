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

"""
create
Update
delete
search
"""
# Strings are immutable -- you can't modify the data once it is created
#
# first_name = "jayanth"
# last_name = "vinay"
#
# print(first_name[0],first_name[1])
# print(first_name[0:4])
# print(first_name[0:])
# print(first_name[2:])
# print(first_name[:4])
# print(first_name[:])
# print(first_name[-1])
# print(first_name[-2])
# print(first_name[-3])
# print("-------------->",first_name[0:-2])
#
#
# # first_name[0] = "H"
# first_name = first_name.replace("j","H")
# print(first_name)
# print(first_name)

# num = 10
# dec = 10.5
#
# print(num + dec)
# # +=,-=,*=
#
# print(type(num))
# print(type(dec))


#list

# ls = [1,20,300]
# ls1 = [9,7,4]
#
# print(ls[0])
# print(ls[0:2])

# ls[0] = 67

# ls.pop(1)
# ls.remove(300)


# print(ls)

# arrays vs list

# ls2 = ["a","b",1,2,["name","age"]]

# tuple

# tup = (1,2,3)
#
# print(tup[0])
# print(tup[0:2])
#
# hyd_location = (17.4122998,78.2679589)
#
# print(tup)

# Relative immutability

# tup = (1,2,["a","b"])
#
# tup[-1].append("c")
# print(tup)

# set
# ls = [1,2,3,4,2,1]
#
# print(ls)
#
#
#
# st = {100,3,5,90,1,6,100}
#
# st.update({10,20})
# st.remove(100)
# print(st)
# print(st)


#Dict

# dic = {"hello":"A greeting key word","name":"indentifier keyword"}
#
# print(dic["hello"])
# print(dic["name"])
#
# # dic["hello"] = "New meaning"
# dic["hello"] += "New meaning"
#
# del dic["name"]
# dic.update({"age":"val","add":{"dr_num":1212,"street":"fghjk567"}})
# print(dic)
# print(dic.keys())
# print(dic.values())
# print(dic.pop("age"))
# print(dic)
import pickletools

# ls1 = [1,2,3]
# ls2 = [20,30,40]
#
# print(ls1 + ls2)
# ls1.append(ls2)
# print(ls1)

num = 9382945438
num1 = "9382945438"
new_num = str(+91)+"-"+str(9382945438)
print(new_num)

print(str(num)[0:-3])
nu = "10"
name = "vinay"
print(int(nu) + 100)
# print(int(name) + 100)

lis = [100,1,2,3,4,1,2]
set_ls = set(lis)
lis = list(set_ls)
lis.sort()
print(lis)

list(set(lis))