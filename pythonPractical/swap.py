#Given a list of numbers of n length, swap the next value by the one divisible by 5
l = int(input("Enter length of the set of numbers : "))
set_n = []
for i in range(0, l):
    set_n.append(int(input("Enter number {}: ".format(i+1))))
for j in range(0, len(set_n)):
    if set_n[j] % 5 == 0:
        set_n[j], set_n[j - 1] = set_n[j - 1], set_n[j]
print("Final list is: ", set_n)
