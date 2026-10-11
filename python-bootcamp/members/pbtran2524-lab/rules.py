from typing import List


def can_register_thesis(credits: int, gpa: float) -> bool:
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> List[str]:
    reasons = []

    if credits < 120:
        needed_credits = 120 - credits
        reasons.append(f"need {needed_credits} more credits")

    if gpa < 2.0:
        reasons.append("gpa must be at least 2.0")

    return reasons


if __name__ == "__main__":
    try:
        user_credits = int(input("Enter the number of credits accumulated: ").strip())
        user_gpa = float(input("Enter the cumulative GPA: ").strip())

        eligible = can_register_thesis(user_credits, user_gpa)
        issues = missing(user_credits, user_gpa)

        print("\n--- RESULT ---")
        print(f"Eligible for thesis registration: {eligible}")
        if issues:
            print(f"Missing requirements: {issues}")
        else:
            print("Congratulations! You meet the requirements for the thesis.")
    except ValueError:
        print("Error: Credits must be an integer and GPA must be a valid float.")