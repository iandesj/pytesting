import csv


class StudentParseError(ValueError):
    pass


class StudentsFileNotFoundError(FileNotFoundError):
    pass


def parse_students_file(filename: str) -> list[dict]:
    try:
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            return list(reader)
    except FileNotFoundError as e:
        raise StudentsFileNotFoundError(f"Could not find file {filename}") from e
