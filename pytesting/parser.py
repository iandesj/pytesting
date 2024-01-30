# parse student names from csv file
import csv


def parse_students_file(filename: str) -> list[dict]:
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        return list(reader)
