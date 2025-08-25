# # Task9
# Example four
seat_number= set(range(1,50))
booked_seat= set()

while True:
    print(f"select from available seat{seat_number}")
    user_input=(input("Book a seat by entering a number(or 'exit'): "))
    if user_input.lower() == 'exit':
        break
# try:
    seat=int(user_input)
    if seat in seat_number:
        booked_seat.add(seat)
        seat_number.discard(seat)
        print(f"congratulations Your seat number {user_input} has been successfully booked!!!")
    else:
       print("Invalid input. Please enter a valid seat number or 'exit'")  
# except ValueError:
    # print("Invalid input. Please enter a valid seat number or 'exit'.")
print("Thank you for booking with us!")
