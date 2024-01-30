import csv


class StudentParseError(ValueError):
    pass


class StudentsFileNotFoundError(FileNotFoundError):
    pass


def parse_students_file(filename: str) -> list[dict]:
    try:
        students = []
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
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
    except ValueError as e:
        raise StudentParseError(f"Could not parse file {filename}") from e
