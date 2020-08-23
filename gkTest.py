marks = []  # Empty List. Created to append marks of individual sections


def generalKnowledge():
    gkCorrectAnswers = 0  # Initial Marks

    while True:
        print("WELCOME TO THE GENERAL KNOWLEDGE TEST\n")  # Basic info
        print("INSTRUCTIONS : \n1.\tTest Consists of 5 Questions\n2.\tEach Question Contains 2 Marks")
        print("3.\tDouble Check While Entering Answer and enter correct Value\n")

        print("\nQuestion : 1")  # Question Starts
        print("Grand Central Terminal, Park Avenue, New York is the world's")
        print(
            "A.	Largest railway station\nB.	Highest railway station\nC.	Longest railway station\nD.	None of the above")
        firstAnswer = input("Enter your Answer [A/B/C/D] : ")  # Enter Answer
        if firstAnswer.upper() == "A":
            gkCorrectAnswers = gkCorrectAnswers + 2  # If correct then add to count
        else:
            pass  # Wrong Answer

        print("\nQuestion : 2")
        print("Entomology is the science that studies")
        print(
            "A.	Behavior of human beings\nB.	Insects\nC.	The origin and history of technical and scientific terms\nD.	The formation of rocks")
        secondAnswer = input("Enter your Answer [A/B/C/D] : ")
        if secondAnswer.upper() == "B":
            gkCorrectAnswers = gkCorrectAnswers + 2
        else:
            pass

        print("\nQuestion : 3")
        print("Eritrea, which became the 182nd member of the UN in 1993, is in the continent of")
        print("A.	Asia\nB.	Africa\nC.	Europe\nD.	Australia")
        thirdAnswer = input("Enter your Answer [A/B/C/D] : ")
        if thirdAnswer.upper() == "B":
            gkCorrectAnswers = gkCorrectAnswers + 2
        else:
            pass

        print("\nQuestion : 4")
        print("Garampani sanctuary is located at")
        print("A.	Junagarh, Gujarat\nB.	Diphu, Assam\nC.	Kohima, Nagaland\nD.	Gangtok, Sikkim")
        fourthAnswer = input("Enter your Answer [A/B/C/D] : ")
        if fourthAnswer.upper() == "B":
            gkCorrectAnswers = gkCorrectAnswers + 2
        else:
            pass

        print("\nQuestion : 5")
        print("For which of the following disciplines is Nobel Prize awarded?")
        print(
            "A.	Physics and Chemistry\nB.	Physiology or Medicine\nC.	Literature, Peace and Economics\nD.	All of the above")
        fifthAnswer = input("Enter your Answer [A/B/C/D] : ")
        if fifthAnswer.upper() == "D":
            gkCorrectAnswers = gkCorrectAnswers + 2
        else:
            pass

        print("\nCONGRATULATIONS. General Knowledge Test Is Over.")
        print(f"Your Score For General Knowledge Test is {gkCorrectAnswers}")
        marks.append(gkCorrectAnswers)

        print("CONGRATULATIONS. YOU HAVE COMPLETED THE TEST.\n")
        break
