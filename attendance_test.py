# Tests for marking student attendance

def test_mark_present():
    student_id = "STU101"
    subject = "Software Testing"
    attendance = "Present"

    assert student_id != ""
    assert subject != ""
    assert attendance in ["Present", "Absent"]

    print("PASS: Attendance details are valid")


def test_mark_absent():
    student_id = "STU102"
    attendance = "Absent"

    assert student_id != ""
    assert attendance == "Absent"

    print("PASS: Absent status is accepted")


def test_invalid_status():
    attendance = "Unknown"

    # Only Present and Absent are allowed
    assert attendance not in ["Present", "Absent"]

    print("PASS: Invalid attendance status detected")


if __name__ == "__main__":
    test_mark_present()
    test_mark_absent()
    test_invalid_status()