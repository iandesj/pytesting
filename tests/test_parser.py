import pytest

from pytesting.parser import (
    StudentParseError,
    StudentsFileNotFoundError,
    parse_students_file,
)


def test_parse_students_file():
    results = parse_students_file("students.csv")
    assert len(results) == 4

    for result in results:
        assert result["first_name"]
        assert result["last_name"]
        assert result["age"]
        assert result["institution"]


def test_parse_students_file_bad_file():
    with pytest.raises(StudentParseError) as e:
        parse_students_file("corrupted_students.csv")


def test_parse_students_file_missing_file():
    with pytest.raises(StudentsFileNotFoundError) as e:
        parse_students_file("nofileexists_students.csv")
