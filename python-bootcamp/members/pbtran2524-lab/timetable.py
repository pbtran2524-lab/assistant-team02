from collections import defaultdict
from typing import Dict, List, Tuple


def group_timetable(timetable: List[Tuple[str, str]]) -> Dict[str, List[str]]:
    grouped = defaultdict(list)

    for course, day in timetable:
        grouped[day].append(course)

    for day in grouped:
        grouped[day].sort()

    return dict(grouped)


if __name__ == "__main__":
    timetable_input = []
    print("Enter your timetable entries in the format 'course_name, day_of_week'.")
    print("Press Enter (leave blank) to finish input.\n")

    while True:
        entry = input("Enter (course, day): ").strip()
        if not entry:
            break

        if "," in entry:
            parts = [p.strip() for p in entry.split(",", 1)]
            course, day = parts[0], parts[1]
            timetable_input.append((course, day))
        else:
            print("Please enter the format with a comma: course_name, day_of_week")

    result = group_timetable(timetable_input)
    print("\n--- RESULT ---")
    print(result)