
# #  Daily Market Report
print("\nDaily Market Report")
# Asking for user input
market_name = input("Enter market name: ")
num_traders = int(input("Enter number of traders: "))
daily_revenue = float(input("Enter daily revenue in naira: "))
# # Displaying result with thousands separator
print(f"\nMarket Name   : {market_name}")
print(f"Traders Count : {num_traders:,}")
print(f"Daily Revenue : ₦{daily_revenue:,.2f}")

