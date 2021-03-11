# a) Write a program containing a function to reverse a user inputted string.

string=input()
stringlength = len(string)
reversedString = string[stringlength::-1] 
print(slicedString)

# b) Write a program containing a function to check if a user inputted number is prime

num = int(input())
if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(num,"is not a prime number")
            break
    else:
        print(num,"is a prime number")
else:
    print(num,"is not a prime number")
