# # task 6
store_items={
    "Pen": 23,
    "biro":30,
    "book":20
}
store_2= store_items.copy()
User_input=input(f"Enter the you will like to buy from us: ")
User_quantity=int(input("Enter the quantity : "))
# After purchase
store_items[User_input] -= User_quantity
print(f"Before purchase {store_2}")
print(f" After purchase {store_items}")
