from utils.exceptions import BackOperation
from utils.validators import Validators
class InputManager:
    @staticmethod
    def get(message):
        value = input(f"{message}: ").strip()
        if value == "0":
            raise BackOperation()
        return value
    @staticmethod
    def text(message):
        while True:
            value = InputManager.get(message)
            if value:
                return value
            print("Input cannot be empty.")
    @staticmethod
    def student_id():
        while True:
            print("Student ID : ST", end="")
            value = input().strip()
            if value == "0":
                raise BackOperation()
            if value.isdigit():
                return "ST" + value
            print("Please enter numbers only.")
    @staticmethod
    def integer(message):
        while True:
            value = InputManager.get(message)
            try:
                return int(value)
            except ValueError:
                print("Please enter a valid integer.")
    @staticmethod
    def decimal(message):
        while True:
            value = InputManager.get(message)
            try:
                return float(value)
            except ValueError:
                print("Please enter a valid number.")
    @staticmethod
    def menu(max_option):
        while True:
            choice = InputManager.integer("Enter Choice")
            if 1 <= choice <= max_option:
                return choice
            print(f"Choose between 1 and {max_option}.")
    @staticmethod
    def cgpa():
        while True:
            value = InputManager.get("CGPA")
            if Validators.validate_cgpa(value):
                return float(value)
            print("CGPA must be between 0 and 10.")
    @staticmethod
    def marks():
        while True:
            value = InputManager.get("Average Marks")
            if Validators.validate_marks(value):
                return float(value)
            print("Marks must be between 0 and 100.")
    @staticmethod
    def attendance():
        while True:
            value = InputManager.get("Attendance (%)")
            if Validators.validate_attendance(value):
                if "%" not in value:
                    value += "%"
                return value
            print("Attendance must be between 0 and 100.")
    @staticmethod
    def yes_no(message):
        while True:
            value = InputManager.get(message).title()
            if Validators.validate_yes_no(value):
                return value
            print("Enter Yes or No.")
    @staticmethod
    def department():
        while True:
            value = InputManager.get("Department").upper()
            if Validators.validate_department(value):
                return value
            print("Invalid Department.")
    @staticmethod
    def year():
        while True:
            value = InputManager.get("Year").upper()
            if Validators.validate_year(value):
                return value
            print("Invalid Year.")