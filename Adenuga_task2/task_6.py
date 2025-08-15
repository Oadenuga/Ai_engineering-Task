
print("*****ELECTRICITY BILL*****")
cus_name = input("Enter your name: ")
unit_cus = int(input("Units consumed (kwh): "))
Cost_per =float(input("Cost per unit(₦): "))
Total_bill = unit_cus * Cost_per
# total format
Total_B = F"₦{Total_bill:,.2f}"
# Display
print('')
print(F" Dear {cus_name} your Total Bill is {Total_B}")
print("Thank you for your payment!!!".center(40, "="))
