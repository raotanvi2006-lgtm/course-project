import sys

def get_student_details(argv):
    # argv[0] is the script name, so we start from argv[1]
    if len(argv) < 4:
        print("Usage: python student.py <name> <program> <semester> <course1:marks> <course2:marks> ...")
        sys.exit(1)

    name = argv[1]
    program = argv[2]
    semester = argv[3]

    # Remaining arguments are courses in the format CourseName:Marks
    courses = []
    for arg in argv[4:]:
        try:
            course_name, marks = arg.split(":")
            marks = int(marks)
            courses.append({"course": course_name, "marks": marks})
        except ValueError:
            print(f"Invalid course format: {arg}. Use CourseName:Marks")
            sys.exit(1)

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
    student = get_student_details(sys.argv)
    display_details(student)
