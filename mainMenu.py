import aptitudeTest
import englishtest
import mathsTest
import gkTest
import marksOfTest

while True:
    try:
        attempts = input("Is this your First Attempt [Y/N] : ")  # Asking Attempts
        if attempts.upper() == "N":  # Break if not first attempt
            print("You can Only Attempt Once. Thank You\n")
            break

        elif attempts.upper() == "Y":  # Perform all operations if 1st Time
            print("\n" + "*" * 20 + "WELCOME TO THE IQ TEST" + "*" * 20)
            print("1.\tAptitude\n2.\tEnglish\n3.\tMath\n4.\tGK\n5.\tExit ") #Printing Menu
            choice = int(input("\nEnter Your Choice : \n"))
            if choice == 1:
                aptitudeTest.aptitude() #Calling a Module
            elif choice == 2:
                englishtest.english()
            elif choice == 3:
                mathsTest.maths()
            elif choice == 4:
                gkTest.generalKnowledge()
            elif choice == 5:
                marksOfTest.marks()
                break
            else:
                print("Invalid Input. Try Again.")

        else:
            print("Invalid Entry.Please Try Again\n")

    except ValueError:  # Error if Integer isn't passed
        print("ERROR : Please Enter a Integer Value\n")

    except Exception:
        print("Something went wrong.Please Try Again.\n")
