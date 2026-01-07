def get_student_details():
    name = input("Enter student name: ")
    program = input("Enter program (e.g., BCA / BSc / BE): ")
    semester = input("Enter semester: ")

    num_courses = int(input("Enter number of courses registered: "))
    courses = []

    for i in range(num_courses):
        print(f"\nCourse {i + 1}")
        course_name = input("Course Name: ")
        marks = int(input("Marks: "))

        courses.append({
            "course": course_name,
            "marks": marks
        })

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