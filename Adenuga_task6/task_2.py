# # # 2
# Unique Name collector
alpha_name=set()
# 
User_name=input("Enter the first name: ")
User_name2=input("Enter the second name: ")
User_name3=input("Enter the third name: ")
# 
alpha_name.add(User_name)
alpha_name.add(User_name2)
alpha_name.add(User_name3)
# 
alpha_names=set(sorted(alpha_name, key= lambda X: X.lower()))
print(alpha_names)