# Task_9
# example three
Balance= 12000
print("Welcome to PayNimbus Utility Service System".center(50, "*"))
code = input("\nEnter USSD '*343*': ").strip()
if code== "*343*":
  while True:
     print("\nChoose an option:\n1. Buy Electricity\n2. Pay Water Bill\n3. Pay Tv subscription\n4. Report Fault\n5. Exit ")
     option=int(input("Input an option: "))

# Ask the user to input an option
     if option==1:
                meter_number= input("Enter your five digits meter number: ")
                if meter_number.isdigit() and len(meter_number)==5:
                    print("\n1.₦300 for 5 kWh\n2.₦600 for 25 kWh\n3.₦900 for 50 kWh\n4.₦5400 for 300kwh\n₦10800 for 900kwh: ")
                    Amount=int(input("Enter Amount: "))
                    if Amount>Balance:
                        print("sorry insufficient Balance")
                        break
                    else:     
                        Balance-=Amount
                        print("Pick a choice:\n1. Confirm\n2. Cancel")
                        choice=int(input("Enter an option: "))
                        if choice==1:
                            print(f"Congratulations User ID: {meter_number} Transaction Successful! Token sent to your phone. New Balance: {Balance}")
                        else:
                            print("❌ Transaction Cancelled.")
                            break
                else:
                    print("Wrong input, please enter a valid Meter number")
                    break

     elif option==2:
            Customer_ID=input("Enter your 10 digits ID: ")
            if Customer_ID.isdigit() and len(Customer_ID)==10:
                Amount=int(input("Enter Amount: "))
                if Amount>Balance:
                    print("sorry insufficient Balance")
                    break
                else:
                 print(f"Congratulations User ID: {Customer_ID} Transaction Successful! Token sent to your phone. New Balance: {Balance}")
            else:
                print("Wrong input, please enter a valid ID number")
                break
     elif option==3:    # Tv subscription
                smart_number= input("Enter your 11 digits Smart card number: ")
                if smart_number.isdigit() and len(smart_number)==11:
                    print("select Tv Provider: \n1. Dstv\n2. Startimes\n3 Exit")
                    Tv_provi=int(input("Select a Tv provider: "))
                    if Tv_provi== 1:
                            print("Welcome to DStv Nigeria Packages")
                            print("a. Premium for ₦15 000\nb. Compact plus for ₦10 000\nc. Compact for ₦8000\nd. confam for ₦5000")
                            Amount=int(input("Enter Amount: "))
                            if Amount>Balance:
                                    print("sorry insufficient Balance")
                                    break
                            else:
                                    Amount-=Balance
                                    print(f"Congratulations User ID:{smart_number} Transaction Successful! New Balance: {Balance}")
                    elif Tv_provi==2:
                        print("Welcome to Startimes Nigeria Packages")
                        print("\na. Premium for ₦15 000\nb. Yanga for ₦10 000\nc. padi for ₦8000\nd. olowokere for ₦5000")
                        Amount=int(input("Enter Amount: "))
                        if Amount>Balance:
                                    print("sorry insufficient Balance")
                                    break
                        else:
                                Amount-=Balance
                                print(f"Congratulations User ID: {smart_number} Transaction Successful! New Balance: {Balance}")  
                    else:
                          print("👋 Thank you for using PayNimbus Utility Services. Goodbye!👌")
                else:     
                     print("Wrong input, please enter a valid smart card number")                 
     elif option == 4:  # Report Fault
                print("1. Electricity\n2. Water\n3. TV")
                service = input("Select Service: ")
                account = input("Enter Account/Meter/Smartcard Number: ")
                description = input("Describe Fault: ")
                print("📌 Thank you! Your complaint has been logged.")
     elif option ==5: # exit 
            print("👋 Thank you for using PayNimbus utility Services. Goodbye!👌")
            break
else:
      print("Invalid code,please enter the correct code👍👍 ")