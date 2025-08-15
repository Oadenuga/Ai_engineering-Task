# # 5
# Shopping list

item1=input("Enter an item you would like to buy: ")
item2=input("Enter an item you would like to buy: ")
item3=input("Enter an item you would like to buy: ")
# creating tople for it
shopping_list=(item1, item2, item3)
# print tuple
print(shopping_list)
# convert to list
con_list=list(shopping_list)
# add
new_items1=input("Enter new item: ")
new_items2=input("Enter new item: ")
# add
con_list.append(new_items1)
con_list.append(new_items2)
# display
print(con_list)
# convert to tuple
new_tuple=tuple(con_list)
print(new_tuple)
# Another approach
new_list=[new_items1, new_items2]
con_list.extend(new_list)
print(con_list)
new_tuple=tuple(con_list)
