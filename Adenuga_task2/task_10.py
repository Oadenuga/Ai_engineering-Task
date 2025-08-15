
# Asking for school details
school_nmame = (input("Enter your school name: "))
# Breakdown of fees to be paid
Tuition_fee = float(input("Enter you tuition fee: "))
Hostel_fee = float(input("Enter you Hostel fee: "))
Feeding_fee = float(input("Enter you Feeding fee: "))
# Total amount
Amount_total = Tuition_fee + Hostel_fee + Feeding_fee
# Receipts printing
print("\n***************************")
print(f"----{school_nmame} school fees receipt")
print(f"Tuition fee: {Tuition_fee:.2f}kb")
print(f"Hostel fee: {Hostel_fee:.2f}kb")
print(f"Feeding fee: {Feeding_fee:.2f}kb")
print(f"The total amount paid into {school_nmame} busery account this session is {Amount_total:.2f}kb")
