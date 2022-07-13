def password_validator(password):
    try:
        lower_flag = False
        upper_flag = False
        num_flag = False
        special_flag = False
        if len(password) < 8:
            raise Exception("Password Should be Minimum of 8 Characters")
        else:
            for each in password:
                if each.islower():
                    lower_flag = True
                if each.isupper():
                    upper_flag = True
                if each.isnumeric():
                    num_flag = True
                if not each.isupper() and not each.islower() and not each.isnumeric():
                    special_flag = True
        if lower_flag and upper_flag and num_flag and special_flag:
            return True
        else:
            return False
    except Exception as e:
        raise Exception(e)
        # raise Exception("Unable to Validate the Password! Please Try again!!!")

print(password_validator("V9c_wertyui"))