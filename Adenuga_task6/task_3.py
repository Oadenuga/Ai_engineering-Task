# # Task 3 simulate a football match tickket system
seat_number= set(range(1,50))
booked_seat= set()

print(seat_number)
User_input=int(input("Book a seat by entering a number: "))

booked_seat.add(User_input)
seat_number.discard(User_input)
print(f"congratulations Your seat number {User_input} has been successfully booked!!!")
print("Thank you for booking with us!")
# print(seat_number.difference(booked_seat))
print(seat_number)
# Another approach
# seat_numbers= set(range(1,50))
# print(f"select from available seat{seat_numbers}")
# # user input
# user_input= int(input("please book a seat by entering a number: "))
# # convert to se
# # con_seat=set(user_input)
# # remove booked 
# print(f"congratulations Your seat number {user_input} has been successfully booked!!!")
# print("Thank you for booking with us!")
# # display Remaining seat
# # print(seat_numbers.difference(con_seat))
# seat_numbers.discard(user_input)
# print(seat_numbers)
