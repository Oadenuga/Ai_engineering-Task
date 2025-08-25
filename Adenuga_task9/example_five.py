# task 9
# example five
print("Welcome to admission checker")
student={}
# user input 
while True:
                    user_name=input("Enter your name: ")
                    User_age=int(input("Enter your age: "))
                    if User_age>=16:
                         print("Congratulations you are eligible for admission")
                         score=input("input your scores separeted by space: ")
                         score_cal=[int (i) for i in score.split()]
                        #  score= int(each_score)
                         average=sum(score_cal)/len(score_cal)
                         if average >= 50:
                                 print("Congratulations you passed your exams🎉🎉🎉")
                                 student["Name"]=user_name
                                 student["Age"]=User_age
                                 student["scores"]= score
                                 student["passed"]= average
                                 print("")
                                 print("Student Record: ")
                                 print("=========================================")
                                 print(f"Name: {student['Name']}\nAge: {student['Age']}\nScores: {score}\nPassed: {student['passed']}")
                                 if student["passed"]>=50:
                                   print(f"I am pleased to inform you {student['Name']},that you have been admitted.Kindly check your mail to accept your admission")
                                   
                                 else:
                                         print("Soryy you didn't meet the cut off")                  
                         else:
                                 print("sorry you are not qualified for this admission")
                    else: 
                            print("Sorry due to age, Your are not qualified for this admission check back next year")

