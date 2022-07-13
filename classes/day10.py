# name = "jayanth vinay"
#pradeep
# print name=[0:6]
#mahitha
# print(name[6])
#Anand
# print(name[:7])
# name[6] = "R"
#pradeep
# ls = [1,2,10,30,40]
# print(ls.pop(2))
# print(ls.remove(40))
# print(ls)
# name[0] = "T"
# name = name.replace("j","T")
# print(name)

# print(name[0])
# len_of_chars = 7
#
# for each in range(len_of_chars):
#     print(name[each],end="")
# print()
# print("hello",end="-")
# print("world")

#j1a1y1a2n1t1h1 v1i1n2a3y2
#a:3,e:0,i:1,o:0,u:0
#count of ovels
#print ovels

# ovels = ["a","e","i","o","u"]
#
# # for each in ovels
# text = input("Enter a string: ")
# for each_char in text:
#     if each_char.lower() in "aeiou":
#         # print(each_char)
#         print(each_char,text.count(each_char))

#for var_name in sequence:
#   statements

person_details = [
    {
    "first_name":"jayanth",
    "last_name":"vinay",
    "phone_num":7013373501,
    "address":{
        "door_num":"22",
        "street_name":"society_colony",
        "mandal":"chittor"
    },
    "hobbies":["music","chess","books"],
    "places_visited":[
        {"name":"tirupathi","when":"1year ago"},
        {"name":"banglore","when":"1month ago"}
    ]
},
    {
    "first_name":"kiran",
    "last_name":"kumar",
    "phone_num":7013373590,
    "address":{
        "door_num":"21",
        "street_name":"balaji_colony",
        "mandal":"tirupathi"
    },
    "hobbies":["cricket","carroms","books"],
    "places_visited":[
        {"name":"tirupathi","when":"3years ago"},
        {"name":"banglore","when":"2months ago"}
    ]
}
]

my_details = {
    "first_name":"jayanth",
    "last_name":"vinay",
    "phone_num":7013373501,
    "address":{
        "door_num":"22",
        "street_name":"society_colony",
        "mandal":"chittor"
    },
    "hobbies":["music","chess","books"],
    "places_visited":[
        {"name":"tirupathi","when":"1year ago"},
        {"name":"banglore","when":"1month ago"}
    ]
}
# print(my_details["hobbies"])
# print(my_details["age"])
print(my_details.get("age"))
for each_person_details in person_details:
    if each_person_details.get("first_name") == "jayanth":
        print(each_person_details["hobbies"])