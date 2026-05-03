def get_student_info():
    name = input("Enter student name: ")
    score = float(input("Enter student score (0-100): "))
    return name, score


def validate_score(score):
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100.")
    return True
