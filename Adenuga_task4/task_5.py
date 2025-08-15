# task 5
student_names = []
student_score = []

student_name1 = input("Enter you name: ")
student_Record1 = int(input("Kindly Enter your score: "))

student_name2= input("Enter you name: ")
student_Record2 = int(input("Kindly Enter your score: "))

student_name3 = input("Enter you name: ")
student_Record3= int(input("Kindly Enter your score: "))

student_names.append(student_name1)
student_names.append(student_name2)
student_names.append(student_name3)

student_score.append(student_Record1)
student_score.append(student_Record2)
student_score.append(student_Record3)

print(student_names)
print(student_score)

print(f"{'Name' :<13} {'score' :<13}")
print("*******************************")
print(f"{student_name1 :<13} {student_Record1}")
print(f"{student_name2 :<13} {student_Record2}")
print(f"{student_name3 :<13} {student_Record3}")
