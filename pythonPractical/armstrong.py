#Program to check whether a given number is armstrong or not
#Taking input from the user
num = input("Enter your number : ")
cmp = 0
for i in num:
       cmp += int(i)**3
if cmp == int(num):
       print("{} is armstrong.".format(cmp))
