from pytesting.parser import parse_students_file


def test_parse_students_file():
    results = parse_students_file("students.csv")
    assert len(results) == 4

    for result in results:
        assert result["name"]
        assert result["age"]
        assert result["school"]
