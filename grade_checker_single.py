def get_student_info():
    name = input("Enter student name: ")
    score = float(input("Enter student score (0-100): "))
    return name, score


def validate_score(score):
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100.")
    return True


def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def get_remark(grade):
    remarks = {
        "A": "Excellent!",
        "B": "Very Good!",
        "C": "Good",
        "D": "Needs Improvement",
        "F": "Fail"
    }
    return remarks[grade]


def display_result(name, score, grade, remark):
    print("\n" + "=" * 35)
    print(f"  Student Name : {name}")
    print(f"  Score        : {score}")
    print(f"  Grade        : {grade}")
    print(f"  Remark       : {remark}")
    print("=" * 35)


def main():
    print("===== Grade Checker Program =====")
    try:
        name, score = get_student_info()
        validate_score(score)
        grade = calculate_grade(score)
        remark = get_remark(grade)
        display_result(name, score, grade, remark)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
