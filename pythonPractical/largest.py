#Find maximum of three numbers
n = 3
n_list = []
for i in range(1, n+1):
    n = int(input("Enter number {}. ".format(i)))
    n_list.append(n)
print("Largest number from the given set is ", max(n_list))
