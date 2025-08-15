# 4 Name Organizer
User_input= input("Please enter five names ")
# split to sort
input_split = User_input.lower().split(" ")
input_split.sort()
for names in input_split:
    print(names)
