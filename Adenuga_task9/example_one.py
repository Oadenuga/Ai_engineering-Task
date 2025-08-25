# Task (9)
# example 1
# Using while true instaed of creating 5 inputs
User_fav= []
# User Inpu7    
while True:
    fav_fruits=input("Kindly Enter your favorite fruit: ")

    if len(fav_fruits) >=1:
        User_fav.append(fav_fruits)
    else:
        print("please enter a valid fruit name")
    if len(User_fav)==5:
        break
print("Your favourite fruits are:", User_fav)