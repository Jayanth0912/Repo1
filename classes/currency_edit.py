num = 400000

for ind,each in enumerate(str(num)):
    if len(str(num)) > 3:
        # val = str(num)[:-3]
        if (len(str(num))-(len(str(num))-ind)) % 2 != 0:
            print(len(str(num))-(len(str(num))-ind))