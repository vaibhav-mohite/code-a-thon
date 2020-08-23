marks = []  # Empty List. Created to append marks of individual sections


def maths():
    mathsCorrectAnswers = 0  # Initial Marks

    while True:
        print("WELCOME TO THE MATHS TEST\n")  # Basic info
        print("INSTRUCTIONS : \n1.\tTest Consists of 5 Questions\n2.\tEach Question Contains 3 Marks")
        print("3.\tDouble Check While Entering Answer and enter correct Value\n")

        print("\nQuestion : 1")  # Question Starts
        print(
            "From a group of 7 men and 6 women, five persons are to be selected to form a committee so that at least 3 men are there on the committee. In how many ways can it be done?")
        print("A.	564\nB.	645\nC.	735\nD.	756")
        firstAnswer = input("Enter your Answer [A/B/C/D] : ")  # If correct then add to count
        if firstAnswer.upper() == "D":
            mathsCorrectAnswers = mathsCorrectAnswers + 3
        else:
            pass  # Wrong Answer

        print("\nQuestion : 2")
        print(
            "In how many different ways can the letters of the word 'LEADING' be arranged in such a way that the vowels always come together?")
        print("A.	810\nB.	1440\nC.	2880\nD.	50400\nE.	5760")
        secondAnswer = input("Enter your Answer [A/B/C/D] : ")
        if secondAnswer.upper() == "D":
            mathsCorrectAnswers = mathsCorrectAnswers + 3
        else:
            pass

        print("\nQuestion : 3")
        print(
            "The ratio between the length and the breadth of a rectangular park is 3 : 2. If a man cycling along the boundary of the park at the speed of 12 km/hr completes one round in 8 minutes, then the area of the park (in sq. m) is:")
        print("A.	15360\nB.	153600\nC.	30720\nD.	307200")
        thirdAnswer = input("Enter your Answer [A/B/C/D] : ")
        if thirdAnswer.upper() == "B":
            mathsCorrectAnswers = mathsCorrectAnswers + 3
        else:
            pass

        print("\nQuestion : 4")
        print(
            "An error 2% in excess is made while measuring the side of a square. The percentage of error in the calculated area of the square is:")
        print("A.	2%\nB.	2.02%\nC.	4%\nD.	4.04%")
        fourthAnswer = input("Enter your Answer [A/B/C/D] : ")
        if fourthAnswer.upper() == "D":
            mathsCorrectAnswers = mathsCorrectAnswers + 3
        else:
            pass

        print("\nQuestion : 5")
        print("The percentage increase in the area of a rectangle, if each of its sides is increased by 20% is:")
        print("A.	40%\nB.	42%\nC.	44%\nD.	46%")
        firstAnswer = input("Enter your Answer [A/B/C/D] : ")
        if firstAnswer.upper() == "C":
            mathsCorrectAnswers = mathsCorrectAnswers + 3
        else:
            pass

        print("\nCONGRATULATIONS. Mathematics Test Is Over. Move On to Next Test.")
        print(f"Your Score For Maths Test is {mathsCorrectAnswers}\n")
        marks.append(mathsCorrectAnswers)
        break
