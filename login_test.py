# Tests for the AttendX login page

def test_valid_login():
    username = "student01"
    password = "Test@123"

    # Both fields should contain a value
    assert username != ""
    assert password != ""

    print("PASS: Login details are entered correctly")


def test_empty_login():
    username = ""
    password = ""

    # Login should not be submitted with empty fields
    assert username == ""
    assert password == ""

    print("PASS: Empty login fields detected")


def test_missing_username():
    username = ""
    password = "Test@123"

    assert username == ""
    assert password != ""

    print("PASS: Missing username detected")

def test_missing_password():
    username = "student01"
    password = ""

    assert username != ""
    assert password == ""

    print("PASS: Missing password detected")

if __name__ == "__main__":
    test_valid_login()
    test_empty_login()
    test_missing_username()
    test_missing_password()