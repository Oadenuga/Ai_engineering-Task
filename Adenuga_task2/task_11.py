print("\nDenuga FX pro: Advance currency converter")
print("welcome to the Nigeria curency converter!")
# exchange rate Details
print("\nPlease provide the following details:\n")
amount_Naira =float(input("Enter amount in Naira: "))
Ex_RD = float(input("Exchange rate to Us dollars: "))
Ex_RB =float(input("Exchange rate to British pounds: "))
# conversion
Naira_Real= amount_Naira 
Naira_USD = amount_Naira * Ex_RD
Naira_BrD = amount_Naira * Ex_RB
print("\n *******Processing*******")
# unit formats
naira_gold = f"#{Naira_Real:,.2f}"
usd_str = f"${Naira_USD:,.2f}"
Brd_str= f"£{Naira_Real:,.2f}"
# Display output
# print(f"Currency\t\tAmount")
# print(f"Naira\t\t{naira_str}")
# print(f"Dollar\t\t{usd_str}")
# print(f"Pound\t\t{Brd_str}")
# Another method of arrangement for Display output 
print(f"{'Currency' :<12}{'Amount' :<15}\n--------------------")
print(f"{'Naira' :<12}{naira_gold :<15}")
print(f"{'Dollar' :<12}{usd_str :<15}")
print(f"{'British' :<12}{Brd_str :<15}")

