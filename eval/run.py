import csv
import os

def evaluate():
    cases_path = os.path.join(os.path.dirname(__file__), 'cases.csv')
    
    if not os.path.exists(cases_path):
        print(f"Error: File {cases_path} not found.")
        return

    correct = 0
    total = 0

    with open(cases_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            input_data = row.get('input') 
            expected_output = row.get('expected')
            total += 1

    if total == 0:
        print("No test cases found.")
        return

    accuracy = (correct / total) * 100
    print(f"Total cases: {total}")
    print(f"Correct: {correct}")
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    evaluate()