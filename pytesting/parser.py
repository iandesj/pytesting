import csv


class StudentParseError(ValueError):
    pass


class StudentsFileNotFoundError(FileNotFoundError):
    pass


def validate_student_data(raw_student: dict) -> None:
    """Validate student data before parsing.

    Args:
        raw_student (dict): The raw student data from the CSV file.

    Raises:
        StudentParseError: If any of the required fields are missing.
    """
    if not bool(raw_student["name"]):
        raise StudentParseError("Name is required")
    if not bool(raw_student["age"]):
        raise StudentParseError("Age is required")
    if not bool(raw_student["school"]):
        raise StudentParseError("School is required")


def convert_raw_student_data(raw_student: dict) -> dict:
    """Convert raw student data to a dictionary.

    Args:
        raw_student (dict): The raw student data from the CSV file.
    """
    first_name, last_name = raw_student["name"].split(" ")
    return {
        "first_name": first_name,
        "last_name": last_name,
        "age": int(raw_student["age"]),
        "institution": raw_student["school"],
    }


def load_students_data_from_file(filename: str) -> list[dict]:
    """Load students data from a CSV file.

    Args:
        filename (str): The name of the CSV file.

    Returns:
        list[dict]: A list of dictionaries containing the student data.
    Raises:
        StudentsFileNotFoundError: If the file does not exist.
    """
    try:
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            return list(reader)
    except FileNotFoundError as e:
        raise StudentsFileNotFoundError(f"Could not find file {filename}") from e


def parse_students_file(filename: str) -> list[dict]:
    """Parse students data from a CSV file.

    Args:
        filename (str): The name of the CSV file.

    Returns:
        list[dict]: The parsed student data in a list.
    """
    students = []
    raw_rows = load_students_data_from_file(filename)
    for row in raw_rows:
        validate_student_data(row)
        student = convert_raw_student_data(row)
        students.append(student)
    return students
