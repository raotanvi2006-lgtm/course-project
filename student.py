def get_student_details():
    # Initialized values
    name = "Tanvi"
    program = "BCA"
    semester = "3"

    # Predefined courses with marks
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
