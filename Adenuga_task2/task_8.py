print("*******🚌 Welcome to the Transport Fare Calculator 🚖*******")
Distance_cov = float(input("Enter Distance Covered (km): "))
price_Km = float(input("price per km ((₦): "))
Total_fae= Distance_cov * price_Km
# Format
Total_fare = F"₦{Total_fae:,.2f}"
print(f"Total Fare: {Total_fare}")

