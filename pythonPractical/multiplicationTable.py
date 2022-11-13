#To print a multiplication table upto n times of a given number
n = int(input("Enter your desired number : "))
x = int(input("Enter the desired length of the table : "))
#print the table.
for i in range(1, x+1):
    print("{} X {} = {}".format(n, i, n*i))
print("------------------")
