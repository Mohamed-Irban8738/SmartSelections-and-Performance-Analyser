from utils.constants import DEPARTMENTS
from utils.constants import YEARS
from utils.constants import YES_NO
class Validators:
    @staticmethod
    def validate_department(department):
        return department in DEPARTMENTS
    @staticmethod
    def validate_year(year):
        return year in YEARS
    @staticmethod
    def validate_yes_no(value):
        return value.title() in YES_NO
    @staticmethod
    def validate_cgpa(value):
        try:
            value = float(value)
            return 0 <= value <= 10
        except:
            return False
    @staticmethod
    def validate_marks(value):
        try:
            value = float(value)
            return 0 <= value <= 100
        except:
            return False
    @staticmethod
    def validate_attendance(value):
        try:
            if value.endswith("%"):
                value = value[:-1]
            value = float(value)
            return 0 <= value <= 100
        except:
            return False
    @staticmethod
    def validate_student_id(student_id):
        if len(student_id) < 4:
            return False
        return student_id.upper().startswith("ST")