# # 4
# Data collection
print("please enter your details")
first_name= input("Enter your first name: ")
age= int(input("Enter your Age: "))
favorite_color= input("Enter your favorite color: ")
Home_add= (input("Enter your Home Address: "))
# tuple list
User_data=(first_name, age, favorite_color, Home_add)
# tuple unpacking
Name,Age,color,Address= User_data
# display
print(f"Name:{Name}\nAge:{Age}\ncolor:{color}\nAddress:{Home_add}")
