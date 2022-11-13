#largest number form usesr defined values
#initialie list
l = []
#take length from user
n = int(input("Enter length: "))
for i in range(1, n+1):
        l.append(int(input("Element {} = ".format(i))))
print("Largest number from given list: ", max(l))
