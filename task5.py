def calculate_average(marks):
    return sum(marks) / len(marks)


def classify_performance(average):
    if average >= 80:
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 60:
        return "Satisfactory"
    else:
        return "Needs Improvement"


def display_report(students):
    for student in students:
        average = calculate_average(student["marks"])
        category = classify_performance(average)
        print(student["id"], student["name"], round(average, 2), category)


students = [
    {"id": 1, "name": "AZIZ", "marks": [85, 90, 78]},
    {"id": 2, "name": "RAKIB", "marks": [72, 68, 75]},
    {"id": 3, "name": "AHNAF", "marks": [60, 65, 58]},
]

display_report(students)