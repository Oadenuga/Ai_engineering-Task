print("Federal Government Scholarship Eligibility Checker")
candidate_name= input("Enter you name: ")
while True:
     citizenship =input("Enter your country?:")
     if citizenship=='Nigeria':
          Enrollment =(input("Are you a full-time undergraduate student in a recognized Nigerian university? (True/false): "))
        
          other_scholarship = (input("Are you currently receiving any scholarship from the oil and gas industry (national or international)? (True/false): "))
          if other_scholarship=='True':
               print("Sorry you are not qualified for this scholarship,we do not allow recipients to recieve our scholarship more than once")
               break
          else:
           Subject_combo=("Mathematics", "English", "Chemistry","Biology", "physics")
           subject1=input(f"Enter your grade in {Subject_combo[0]}: ").upper()
           subject2=input(f"Enter your grade in {Subject_combo[2]}: ").upper()
           subject3=input(f"Enter your grade in {Subject_combo[3]}: ").upper()
           subject4=input(f"Enter your grade in {Subject_combo[1]}: ").upper()
           subject5=input(f"Enter your grade in {Subject_combo[4]}: ").upper()
           Qualification= ((subject1== 'A') or (subject1== 'B')) and ((subject2== 'A') or  (subject2== 'B')) and ((subject3== 'A') or (subject3== 'B')) and ((subject4== 'A') or (subject4== 'B')) and ((subject5== 'A')or (subject5== 'B'))
           if Qualification== False: 
                  print("Sorry you do not have the complete O'level requirement")   
                  break
           else:
             print(Qualification)
             Eligibility = (Enrollment.lower()== 'true' and other_scholarship.lower() == 'false' and citizenship.title() =='Nigeria' and Qualification == True)
             print(Eligibility)
             print(f"candidate: {candidate_name}\nNigerian citizen?: {citizenship}\nEnrollment: {Enrollment}\nBenefitted from other scholrship: {other_scholarship}\nQualified: {Qualification}\nEligibility:{Eligibility}")
             print("")
             if Eligibility == True:
              print("🎉🎉Congratulations you are eligible for this scholarship!!")
             if Eligibility==False:
                print("🎉🎉Congratulations you are Not eligible for this scholarship!!")
                break
     else:
        print("sorry,you are not qualified for this scholarship😔😔")
        break