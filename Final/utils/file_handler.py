import csv
import os
from models.student import Student
class FileHandler:
    def __init__(self, filename):
        self.filename = filename
    def load(self):
        students = []
        if not os.path.exists(self.filename):
            return students
        with open(
            self.filename,
            newline="",
            encoding="utf-8"
        ) as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(
                    Student.from_dict(row)
                )
        return students
    def save(self, students):
        if len(students) == 0:
            return
        with open(
            self.filename,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:
            writer = csv.DictWriter(
                file,
                fieldnames=students[0].to_dict().keys()
            )
            writer.writeheader()
            for student in students:
                writer.writerow(
                    student.to_dict()
                )