def calculate_average(marks):
    if not marks:   # handle empty list
        return 0
    return sum(marks) / len(marks)


def placement_eligibility(avg):
    if avg >= 75:
        return "Eligible for Placement"
    elif avg >= 60:
        return "Eligible for Internship"
    else:
        return "Not Eligible"


def get_student_details():
    name = "Tanvi"
    program = "BCA"
    semester = "3"

    courses = [
        {"course": "Math", "marks": 99},
        {"course": "Physics", "marks": 98},
        {"course": "CS", "marks": 90}
    ]

    return {
        "name": name,
        "program": program,
        "semester": semester,
        "courses": courses
    }


def display_details(student):
    print("\n========== STUDENT DETAILS ==========")
    print(f"Name     : {student['name']}")
    print(f"Program  : {student['program']}")
    print(f"Semester : {student['semester']}")

    print("\nCourse Details:")
    for c in student["courses"]:
        if c["marks"] < 50:
            print(f"{c['course']} - {c['marks']} (Failed)")
        else:
            print(f"{c['course']} - {c['marks']}")
    print("====================================")


if __name__ == "__main__":
    student = get_student_details()
    display_details(student)

    # Example usage of new functions
    marks = [c["marks"] for c in student["courses"]]
    avg = calculate_average(marks)
    print("Average:", avg)
    print("Eligibility:", placement_eligibility(avg))
