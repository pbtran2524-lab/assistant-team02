import statistics
from typing import Dict, List


def grade_summary(scores: List[float]) -> Dict[str, float]:
    if not scores:
        raise ValueError("The list of scores cannot be empty.")

    min_val = round(min(scores), 2)
    max_val = round(max(scores), 2)
    mean_val = round(sum(scores) / len(scores), 2)
    median_val = round(statistics.median(scores), 2)

    return {
        "min": min_val,
        "max": max_val,
        "mean": mean_val,
        "median": median_val,
    }

if __name__ == "__main__":
    raw_input = input("Enter the list of scores (separated by spaces): ").strip()

    if raw_input:
        scores = [float(x) for x in raw_input.split()]
        
        result = grade_summary(scores)
        print("Result:", result)
    else:
        print("Invalid. Please provide a list of scores.")