"""
Difference between List & Tuple?

"""


# ls = [(10,20,30),(100,200,300)]
# tup = ([110,120,130],[190,200,210])
# (a,b,c) or ({},{},{}) or ([],[],[]) or ((),(),())

# ls2 = [1,2,3]
# ls2.append(100)
# ls2[1] = 90
# print(ls2)
#
# tup2 = (1,2,3)
# tup2[1] = 90














# ls.append(100)
# tup.append(100)

# print(ls[0])
# ls[0] = "wertyuiop"
# print(ls[0][0])
# ls[0][0] = "456789"
# tup[0][0] = 9283734
# print(tup)
# print(ls)

# sat_att_students_ls = ["Pradeep","mahitha","baba","anand","bharath","kiran","mukesh","pavani","suresh","vijay"]
#
# # "in" / "not in"
#
# # print("Kiran".lower() in sat_att_students_ls)
#
# try:
#     for eachstudent in sat_att_students_ls:
#         if type(eachstudent) == str and eachstudent.lower() == "kiran":
#             print("Kiran attended the class saturday")
#             break
#         print(eachstudent)
# except Exception as e:
#     raise Exception(e)



# print(isinstance(sat_att_students_ls,list))
# print(type(sat_att_students_ls) == list)
#




js = [
	{
		"id": "0001",
		"type": "donut",
		"name": "Cake",
		"ppu": 0.55,
		"batters":
			{
				"batter":
					[
						{ "id": "1001", "type": "Regular" },
						{ "id": "1002", "type": "Chocolate" },
						{ "id": "1003", "type": "Blueberry" },
						{ "id": "1004", "type": "Devil's Food" }
					]
			},
		"topping":
			[
				{ "id": "5001", "type": "None" },
				{ "id": "5002", "type": "Glazed" },
				{ "id": "5005", "type": "Sugar" },
				{ "id": "5007", "type": "Powdered Sugar" },
				{ "id": "5006", "type": "Chocolate with Sprinkles" },
				{ "id": "5003", "type": "Chocolate" },
				{ "id": "5004", "type": "Maple" }
			]
	},
	{
		"id": "0002",
		"type": "donut",
		"name": "Raised",
		"ppu": 0.55,
		"batters":
			{
				"batter":
					[
						{ "id": "1001", "type": "Regular" }
					]
			},
		"topping":
			[
				{ "id": "5001", "type": "None" },
				{ "id": "5002", "type": "Glazed" },
				{ "id": "5005", "type": "Sugar" },
				{ "id": "5003", "type": "Chocolate" },
				{ "id": "5004", "type": "Maple" }
			]
	},
	{
		"id": "0003",
		"type": "donut",
		"name": "Old Fashioned",
		"ppu": 0.55,
		"batters":
			{
				"batter":
					[
						{ "id": "1001", "type": "Regular" },
						{ "id": "1002", "type": "Chocolate" }
					]
			},
		"topping":
			[
				{ "id": "5001", "type": "None" },
				{ "id": "5002", "type": "Glazed" },
				{ "id": "5003", "type": "Chocolate" },
				{ "id": "5004", "type": "Maple" }
			]
	}
]

# user_input : type of recipe: "Old Fashioned"
# Regular , Chocolate
# user_input : type of recipe: "Old Fashioned"
# None, Glazed, chocolate, maple