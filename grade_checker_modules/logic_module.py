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
        "F": "Failing — Please seek help."
    }
    return remarks[grade]
