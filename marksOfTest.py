import aptitudeTest
import englishtest
import mathsTest
import gkTest


def marks():
    totalMarks = aptitudeTest.marks[0] + englishtest.marks[0] + mathsTest.marks[0] + gkTest.marks[0]  # Adding Marks of All Sections
    print(f"Mark Obtained : {totalMarks}")  # Marks before Bonus

    # Seperating by Conditions
    if 20 < totalMarks < 30:
        totalMarks = totalMarks + 2  # Adding Bonus Marks
        print("Bonus Marks : 2")

        if totalMarks == 0:
            print("REMARKS : You Need to Reappear to the test")
        elif 10 < totalMarks < 20:
            print("REMARKS : Your IQ is Below Average")
        elif 20 < totalMarks < 30:
            print("REMARKS : Your IQ is Average")
        elif 30 < totalMarks < 40:
            print("REMARKS : You are Intelligent")
        elif 40 < totalMarks < 50:
            print("REMARKS : You are Genius")
        else:
            pass
        print(f"Final Marks Obtained Are : {totalMarks}")

    elif 30 < totalMarks < 40:
        totalMarks = totalMarks + 5
        print("Bonus Marks : 5")

        if totalMarks == 0:
            print("You Need to Reappear to the test")
        elif 10 < totalMarks < 20:
            print("REMARKS : Your IQ is Below Average")
        elif 20 < totalMarks < 30:
            print("REMARKS : Your IQ is Average")
        elif 30 < totalMarks < 40:
            print("REMARKS : You are Intelligent")
        elif 40 < totalMarks < 50:
            print("REMARKS : You are Genius")
        else:
            pass
        print(f"Final Marks Obtained Are : {totalMarks}")

    elif totalMarks > 40:
        print(f"Bonus Marks : {50 - totalMarks}")
        print(f"Final Marks Obtained Are : 50")
        print("REMARKS : You are a Genius")

    else:
        pass
