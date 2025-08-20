# # task 4
student={}
# user input 
user_name=input("Enter your name: ")
User_age=int(input("Enter your age: "))
score=[70, 60, 50]
student["Name"]=user_name
student["Age"]=User_age
student["scores"]= score
average=(sum(score)/len(score))>= 50
student["passed"]= average
student["Teen_age"]=student["Age"] in range(13,19)

print(student)
print("")
print("Student Record: ")
print(f"Name: {student['Name']}\nAge: {student['Age']}\nScores: {score}\nPassed: {student['passed']}\nTeenager: {student['Teen_age']}")
if student==True:
    print("congratulations you passed your exams🎉🎉")
else:
    print("you failed ")
