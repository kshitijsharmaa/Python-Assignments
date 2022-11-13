#Print a number pyramid with the numbers being in order
n = int(input("Enter the length: "))
x = 1
#using nested loops to generate the patter, x will be the medium
#through which we will have consecutive numbers
for i in range(1, n+1):
    for j in range(1, i+1):
        print(x, end = ' ')
        x += 1
    print()
