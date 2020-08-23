marks = []  # Empty List. Created to append marks of individual sections


def english():
    englishCorrectAnswers = 0  # Initial Marks

    while True:
        print("WELCOME TO THE ENGLISH TEST\n")  # Basic info
        print("INSTRUCTIONS : \n1.\tTest Consists of 5 Questions\n2.\tEach Question Contains 2 Marks")
        print("3.\tDouble Check While Entering Answer and enter correct Value\n")

        print("Question : 1")  # Question Starts
        print("Synonym : CORPULENT")
        print("A.	Lean\nB.	Gaunt\nC.	Emaciated\nD.	Obese")
        firstAnswer = input("Enter your Answer [A/B/C/D] : ")  # Enter Answer
        if firstAnswer.upper() == "D":
            englishCorrectAnswers = englishCorrectAnswers + 2  # If correct then add to count
        else:
            pass  # Wrong Answer

        print("\nQuestion : 2")
        print("Synonym : EMBEZZLE")
        print("A.	Misappropriate\nB.	Balance\nC.	Remunerate\nD.	Clear")
        secondAnswer = input("Enter your Answer [A/B/C/D] : ")
        if secondAnswer.upper() == "A":
            englishCorrectAnswers = englishCorrectAnswers + 2
        else:
            pass

        print("\nQuestion : 3")
        print("One Word Substitute : Extreme old age when a man behaves like a fool")
        print("A.	Imbecility\nB.	Senility\nC.	Dotage\nD.	Superannuation")
        thirdAnswer = input("Enter your Answer [A/B/C/D] : ")
        if thirdAnswer.upper() == "C":
            englishCorrectAnswers = englishCorrectAnswers + 2
        else:
            pass

        print("\nQuestion : 4")
        print("One Word Substitute : The study of ancient societies")
        print("A.	Anthropology\nB.	Archaeology\nC.	History\nD.	Ethnology")
        fourthAnswer = input("Enter your Answer [A/B/C/D] : ")
        if fourthAnswer.upper() == "B":
            englishCorrectAnswers = englishCorrectAnswers + 2
        else:
            pass

        print("\nQuestion : 5")
        print("Find the correctly spelt words")
        print("A.	Efficient\nB.	Treatmeant\nC.	Beterment\nD.	Employd")
        fifthAnswer = input("Enter your Answer [A/B/C/D] : ")
        if fifthAnswer.upper() == "A":
            englishCorrectAnswers = englishCorrectAnswers + 2
        else:
            pass

        print("\nCONGRATULATIONS. English Test Is Over. Move On to Next Test.")
        print(f"Your Score For English Test is {englishCorrectAnswers}\n")
        marks.append(englishCorrectAnswers)
        break
