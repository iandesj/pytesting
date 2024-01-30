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


def parse_students_file(filename: str) -> list[dict]:
    try:
        students = []
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                validate_student_data(row)
                first_name, last_name = row["name"].split(" ")
                students.append(
                    {
                        "first_name": first_name,
                        "last_name": last_name,
                        "age": row["age"],
                        "institution": row["school"],
                    }
                )
            return students
    except FileNotFoundError as e:
        raise StudentsFileNotFoundError(f"Could not find file {filename}") from e
