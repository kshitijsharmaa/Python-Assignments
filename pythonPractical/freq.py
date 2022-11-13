#Print freq of each element in a given list
#initialize list
l = []
#request desired length of list
n = int(input("Enter length of list: "))
for i in range(0, n):
    l.append(int(input("Enter element {}: ".format(i+1))))
print("------------------------")
#Create a list with all the unique elements from l
cmp_l = list(dict.fromkeys(l))
#iterate through each element of the new list and check the count
#of each element in the original list and print it.
for j in range(0, len(cmp_l)):
    print(cmp_l[j], "Count = ", l.count(cmp_l[j]))
print("------------------------")
