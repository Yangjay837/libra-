def calculate_grade(subject1, subject2, subject3):

    average_score = (subject1 + subject2 + subject3) / 3

    if average_score < 0:
        print("ERROR: Negative average score")
        return
    elif average_score > 100:
        print("ERROR: Average score greater than 100")
        return

    
    if 70 <= average_score <= 100:
        grade = "A"
    elif 60 <= average_score < 70:
        grade = "B"
    elif 50 <= average_score < 60:
        grade = "C"
    elif 40 <= average_score < 50:
        grade = "D"
    elif 0 <= average_score < 40:
        grade = "FAIL"
    else:
        grade = "ERROR: Invalid average score"

    
    print(f"Subject1: {subject1}")
    print(f"Subject2: {subject2}")
    print(f"Subject3: {subject3}")
    print(f"Average Score: {average_score}")
    print(f"Grade: {grade}")


subject1 = int(input("Enter marks for subject 1: "))
subject2 = int(input("Enter marks for subject 2: "))
subject3 = int(input("Enter marks for subject 3: "))


calculate_grade(subject1, subject2, subject3)