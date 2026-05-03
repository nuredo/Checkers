from input_module import get_student_info, validate_score
from logic_module import calculate_grade, get_remark
from output_module import display_result


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
