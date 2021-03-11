# e) Write a program containing a function to check if a user inputted string is a good
#    password or not, if not have them try again. A password is considered good if it
#    contains at least 7 characters and 2 of those are either a number or special
#    character(by special character I mean any one of the characters on the numbers
#    1-8, i.e. !@#$%^&*).


import re
p= input("Input your password")
x = True
count = 0
if(len(p)>7):
    for i in range(len(p)):  
        if re.search("[0-9]",p):
            count += 1
        if re.search("[!@#$%^&*]",p):
            count += 1

    if(count >= 2):
        print("Valid Password")
        x = False
if x:
    print("Not a Valid Password")