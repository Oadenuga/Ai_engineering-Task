# 1
num1 =int(input("Enter first number"))
num2 =int(input("Enter you second number"))
# 
print(f"{num1} == {num2} : {num1 == num2}") #compares if the two nubers are equal

print(f"{num1} !={num2} : {num1 != num2}")  #compares if the two numbers are not equal

print(f"{num1} > {num2}: {num1 > num2}") # check if number 1 is > num 2

print(f"{num1}, {num2} : {num1 < num2} ") #check if number 1 is < number 2

# Grading system
# authenication system
# price cpomparism 

# Grading system
student_score = int(input("Enter your score: "))
passing_score = 60

print(f"{student_score}=={passing_score}:{student_score==passing_score}")
print(f"{student_score}!={passing_score}:{student_score!=passing_score}")
print(f"{student_score}>{passing_score}:{student_score>passing_score}")
print(f"{student_score}<{passing_score}:{student_score<passing_score}")
print(" ")
# display
if student_score >= passing_score:
    print("congratulations you passed")
else:
    print("You failed")