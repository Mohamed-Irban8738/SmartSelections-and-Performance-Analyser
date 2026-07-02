import os
class UI:
    WIDTH = 80
    @staticmethod
    def clear():
        os.system("cls" if os.name == "nt" else "clear")
    @staticmethod
    def line(char="═"):
        print(char * UI.WIDTH)
    @staticmethod
    def title(title):
        UI.clear()
        UI.line()
        print(title.center(UI.WIDTH))
        UI.line()
    @staticmethod
    def section(title):
        print()
        UI.line("-")
        print(title)
        UI.line("-")
    @staticmethod
    def success(msg):
        print(f"\n[SUCCESS] {msg}")
    @staticmethod
    def error(msg):
        print(f"\n[ERROR] {msg}")
    @staticmethod
    def warning(msg):
        print(f"\n[WARNING] {msg}")
    @staticmethod
    def info(msg):
        print(f"\n[INFO] {msg}")
    @staticmethod
    def pause():
        input("\nPress ENTER to continue...")
    @staticmethod
    def student_card(student):
        UI.line()
        print(f"{'ID':20}: {student.id}")
        print(f"{'Name':20}: {student.name}")
        print(f"{'Department':20}: {student.department}")
        print(f"{'Year':20}: {student.year}")
        print(f"{'CGPA':20}: {student.cgpa}")
        print(f"{'Skills':20}: {student.skills}")
        print(f"{'Certifications':20}: {student.certifications}")
        print(f"{'Events':20}: {student.previous_events}")
        print(f"{'Attendance':20}: {student.attendance}")
        print(f"{'Average Marks':20}: {student.average_marks}")
        print(f"{'Scholarship':20}: {student.scholarship}")
        print(f"{'Placement':20}: {student.placement_eligible}")
        UI.line()
    @staticmethod
    def table(students):
        if len(students) == 0:
            UI.warning("No Records Found.")
            return
        UI.line()
        print(
            f"{'ID':<10}"
            f"{'Name':<20}"
            f"{'Dept':<10}"
            f"{'Year':<6}"
            f"{'CGPA':<8}"
        )
        UI.line()
        for student in students:
            print(
                f"{student.id:<10}"
                f"{student.name:<20}"
                f"{student.department:<10}"
                f"{student.year:<6}"
                f"{student.cgpa:<8}"
            )
        UI.line()
    @staticmethod
    def statistics(data):
        UI.line()
        for key, value in data.items():
            print(f"{key:<30}: {value}")
        UI.line()