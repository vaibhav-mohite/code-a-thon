marks = []  # Empty List. Created to append marks of individual sections


def aptitude():
    aptitudeCorrectAnswers = 0  # Initial Marks

    while True:
        print("WELCOME TO THE APTITUDE TEST\n")  # Basic info
        print("INSTRUCTIONS : \n1.\tTest Consists of 5 Questions\n2.\tEach Question Contains 3 Marks")
        print("3.\tDouble Check While Entering Answer and enter correct Value\n")

        print("Question : 1")  # Question Starts
        print("A Train running at the speed of 60 km/hr crosses a pole in 9 seconds. What is the length of the train?")
        print("A.	120 metres\nB.	180 metres\nC.	324 metres\nD.	150 metres")
        firstAnswer = input("Enter your Answer [A/B/C/D] : ")  # Enter Answer
        if firstAnswer.upper() == "D":
            aptitudeCorrectAnswers = aptitudeCorrectAnswers + 3  # If correct then add to count
        else:
            pass  # Wrong Answer

        print("\nQuestion : 2")
        print(
            "A train 125 m long passes a man, running at 5 km/hr in the same direction in which the train is going, in 10 seconds.The speed of the train is:")
        print("A.	45 km/hr\nB.	50 km/hr\nC.	54 km/hr\nD.	55 km/hr")
        secondAnswer = input("Enter your Answer [A/B/C/D] : ")
        if secondAnswer.upper() == "B":
            aptitudeCorrectAnswers = aptitudeCorrectAnswers + 3
        else:
            pass

        print("\nQuestion : 3")
        print("A person crosses a 600 m long street in 5 minutes. What is his speed in km per hour?")
        print("A.	3.6\nB.	7.2\nC.	8.4\nD.	10")
        thirdAnswer = input("Enter your Answer [A/B/C/D] : ")
        if thirdAnswer.upper() == "B":
            aptitudeCorrectAnswers = aptitudeCorrectAnswers + 3
        else:
            pass

        print("\nQuestion : 4")
        print(
            "An aeroplane covers a certain distance at a speed of 240 kmph in 5 hours. To cover the same distance in 1 hours, it must travel at a speed of:")
        print("A.	300 kmph\nB.	360 kmph\nC.	600 kmph\nD.	720 kmph")
        fourthAnswer = input("Enter your Answer [A/B/C/D] : ")
        if fourthAnswer.upper() == "D":
            aptitudeCorrectAnswers = aptitudeCorrectAnswers + 3
        else:
            pass

        print("\nQuestion : 5")
        print(
            "If a person walks at 14 km/hr instead of 10 km/hr, he would have walked 20 km more. The actual distance travelled by him is:")
        print("A.	50 km\nB.	56 km\nC.	70 km\nD.	80 km")
        fifthAnswer = input("Enter your Answer [A/B/C/D] : ")
        if fifthAnswer.upper() == "A":
            aptitudeCorrectAnswers = aptitudeCorrectAnswers + 3
        else:
            pass

        print("\nCONGRATULATIONS. Aptitude Test Is Over. Move On to Next Test.")  # Printing Info
        print(f"Your Score For Aptitude Test is {aptitudeCorrectAnswers}\n")
        marks.append(aptitudeCorrectAnswers)  # Appending total count to empty list
        break
