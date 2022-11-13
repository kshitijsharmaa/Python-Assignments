#Ask input
customer_no = int(input("Enter customer ID: "))
units = int(input("Enter units consumed: "))
print("----------------------------------------")
print("              The Company               ")
print("----------------------------------------")
charge = 0
#Calculating the fee
if units > 0 and units <= 100:
    charge = units * 1
elif units >= 101 and units <= 300:
    charge = 100 + (units % 100) * 1.25
elif units >= 301 and units <= 500:
    charge = 350 + (units % 300) * 1.5
else :
    charge = 650 + (units % 500) * 1.75
print("Customer ID : ", customer_no)
print("Units Consumed : ", units)
print("Bill (excl. taxes) : ", charge)
print("----------------------------------------")
