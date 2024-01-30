from pytesting.parser import parse_students_file


def test_parse_students_file():
    result = parse_students_file("students.csv")
    assert result
