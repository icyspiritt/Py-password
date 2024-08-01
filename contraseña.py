import random

def create_password(pass_Lenght):
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""
    for i in range(pass_Lenght):
        password += random.choice(elements)
    print (password)
create_password(15)
