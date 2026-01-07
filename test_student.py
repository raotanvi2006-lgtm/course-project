from student import calculate_average, placement_eligibility

def test_average_marks():
    marks = [60, 70, 80]
    assert calculate_average(marks) == 70

def test_average_empty():
    marks = []
    assert calculate_average(marks) == 0

def test_placement_eligible():
    avg = 78
    assert placement_eligibility(avg) == "Eligible for Placement"

def test_internship_eligible():
    avg = 65
    assert placement_eligibility(avg) == "Eligible for Internship"

def test_not_eligible():
    avg = 50
    assert placement_eligibility(avg) == "Not Eligible"