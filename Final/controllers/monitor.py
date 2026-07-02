from models.student import Student
from services.analytics import Analytics
from services.recommendation import RecommendationEngine
from services.event import EventService
from utils.file_handler import FileHandler
from utils.ui import UI
from utils.input_manager import InputManager
from utils.decorators import back_handler
class Monitor:
    def __init__(self):
        self.file = FileHandler("data/student_db.csv")
        self.students = self.file.load()
        self.analytics = Analytics()
        self.recommendation = RecommendationEngine()
        self.event = EventService()
    def refresh(self):
        self.students = self.file.load()
    def save(self):
        self.file.save(self.students)
    def find_student(self, student_id):
        for student in self.students:
            if student.id.lower() == student_id.lower():
                return student
        return None
    def student_exists(self, student_id):
        return self.find_student(student_id) is not None
    def display_students(self, students=None):
        if students is None:
            students = self.students
        if len(students) == 0:
            UI.warning("No Student Records Found.")
            return
        UI.table(students)
    def display_student(self, student):
        if student:
            UI.student_card(student)
        else:
            UI.error("Student Not Found.")
    @back_handler
    def add_student(self):
        UI.title("Add Student")
        self.refresh()
        student_id = InputManager.student_id()
        if self.student_exists(student_id):
            UI.error("Student ID already exists.")
            UI.pause()
            return
        name = InputManager.text("Student Name")
        department = InputManager.department()
        year = InputManager.year()
        cgpa = InputManager.cgpa()
        skills = InputManager.text(
            "Skills (Comma Separated)"
        )
        certifications = InputManager.text(
            "Certifications (Comma Separated)"
        )
        previous_events = InputManager.text(
            "Previous Events (Comma Separated)"
        )
        attendance = InputManager.attendance()
        average_marks = InputManager.marks()
        scholarship = InputManager.yes_no(
            "Scholarship (Yes/No)"
        )
        placement = InputManager.yes_no(
            "Placement Eligible (Yes/No)"
        )
        student = Student(
            student_id,
            name,
            department,
            year,
            cgpa,
            skills,
            certifications,
            previous_events,
            attendance,
            average_marks,
            scholarship,
            placement
        )
        self.students.append(student)
        self.save()
        UI.success("Student Added Successfully.")
        UI.pause()
    @back_handler
    def view_students(self):
        UI.title("View Students")
        self.refresh()
        if not self.students:
            UI.warning("No Student Records Found.")
            UI.pause()
            return
        while True:
            UI.table(self.students)
            print("\n1. View Student Details")
            print("0. Back")
            choice = InputManager.menu(1)
            if choice == 1:
                student_id = InputManager.text(
                    "Enter Student ID"
                )
                student = self.find_student(student_id)
                if student:
                    UI.student_card(student)
                else:
                    UI.error("Student Not Found.")
                UI.pause()
    @back_handler
    def search_student(self):
        UI.title("Search Student")
        print("Search By")
        print("1. Student ID")
        print("2. Student Name")
        print("3. Department")
        print("4. Skill")
        print("5. Certification")
        choice = InputManager.menu(5)
        result = []
        if choice == 1:
            student_id = InputManager.text(
                "Student ID"
            )
            student = self.find_student(student_id)
            if student:
                UI.student_card(student)
            else:
                UI.error("Student Not Found.")
            UI.pause()
            return
        elif choice == 2:
            keyword = InputManager.text(
                "Student Name"
            ).lower()
            result = [
                student
                for student in self.students
                if keyword in student.name.lower()
            ]
        elif choice == 3:
            department = InputManager.department()
            result = [
                student
                for student in self.students
                if student.department == department
            ]
        elif choice == 4:
            keyword = InputManager.text(
                "Skill"
            ).lower()
            result = [
                student
                for student in self.students
                if keyword in student.skills.lower()
            ]
        elif choice == 5:
            keyword = InputManager.text(
                "Certification"
            ).lower()
            result = [
                student
                for student in self.students
                if keyword in student.certifications.lower()
            ]
        if len(result) == 0:
            UI.warning("No Matching Students Found.")
        else:
            UI.table(result)
        UI.pause()
    @back_handler
    def update_student(self):
        UI.title("Update Student")
        self.refresh()
        student_id = InputManager.text(
            "Enter Student ID"
        )
        student = self.find_student(student_id)
        if student is None:
            UI.error("Student Not Found.")
            UI.pause()
            return
        while True:
            print("\nSelect Field")
            print("1. Name")
            print("2. Department")
            print("3. Year")
            print("4. CGPA")
            print("5. Skills")
            print("6. Certifications")
            print("7. Previous Events")
            print("8. Attendance")
            print("9. Average Marks")
            print("10. Scholarship")
            print("11. Placement Eligible")
            choice = InputManager.menu(11)
            fields = {
                1: "name",
                2: "department",
                3: "year",
                4: "cgpa",
                5: "skills",
                6: "certifications",
                7: "previous_events",
                8: "attendance",
                9: "average_marks",
                10: "scholarship",
                11: "placement_eligible"
            }
            field = fields[choice]
            if field == "department":
                value = InputManager.department()
            elif field == "year":
                value = InputManager.year()
            elif field == "cgpa":
                value = InputManager.cgpa()
            elif field == "attendance":
                value = InputManager.attendance()
            elif field == "average_marks":
                value = InputManager.marks()
            elif field in ["scholarship", "placement_eligible"]:
                value = InputManager.yes_no(
                    "Enter Value"
                )
            else:
                value = InputManager.text(
                    "Enter New Value"
                )
            student.update(field, value)
            self.save()
            UI.success("Student Updated Successfully.")
            UI.pause()
            return
    @back_handler
    def delete_student(self):
        UI.title("Delete Student")
        self.refresh()
        student_id = InputManager.text(
            "Enter Student ID"
        )
        student = self.find_student(student_id)
        if student is None:
            UI.error("Student Not Found.")
            UI.pause()
            return
        UI.student_card(student)
        confirm = InputManager.yes_no(
            "Are you sure you want to delete this student? (Yes/No)"
        )
        if confirm.lower() == "yes":
            self.students.remove(student)
            self.save()
            UI.success("Student Deleted Successfully.")
        else:
            UI.info("Deletion Cancelled.")
        UI.pause()
    @back_handler
    def filter_students(self):
        UI.title("Filter Students")
        self.refresh()
        print("Filter By")
        print("1. Department")
        print("2. Year")
        print("3. Minimum CGPA")
        print("4. Attendance")
        print("5. Skill")
        print("6. Scholarship")
        print("7. Placement Eligible")
        choice = InputManager.menu(7)
        result = []
        if choice == 1:
            department = InputManager.department()
            result = [
                student
                for student in self.students
                if student.department.lower() == department.lower()
            ]
        elif choice == 2:
            year = InputManager.year()
            result = [
                student
                for student in self.students
                if student.year.upper() == year.upper()
            ]
        elif choice == 3:
            cgpa = InputManager.cgpa()
            result = [
                student
                for student in self.students
                if student.cgpa >= cgpa
            ]
        elif choice == 4:
            attendance = float(
                InputManager.attendance().replace("%", "")
            )
            result = [
                student
                for student in self.students
                if student.attendance_percent >= attendance
            ]
        elif choice == 5:
            skill = InputManager.text(
                "Enter Skill"
            ).lower()
            result = [
                student
                for student in self.students
                if skill in student.skills.lower()
            ]
        elif choice == 6:
            scholarship = InputManager.yes_no(
                "Scholarship (Yes/No)"
            )
            result = [
                student
                for student in self.students
                if student.scholarship.lower() == scholarship.lower()
            ]
        elif choice == 7:
            placement = InputManager.yes_no(
                "Placement Eligible (Yes/No)"
            )
            result = [
                student
                for student in self.students
                if student.placement_eligible.lower() == placement.lower()
            ]
        if len(result) == 0:
            UI.warning("No Matching Students Found.")
        else:
            UI.table(result)
        UI.pause()
    @back_handler
    def group_students(self):
        UI.title("Group Students")
        self.refresh()
        print("Group By")
        print("1. Department")
        print("2. Performance")
        print("3. Year")
        print("4. Placement Eligible")
        print("5. Scholarship")
        choice = InputManager.menu(5)
        if choice == 1:
            department = InputManager.department()
            students = [
                student
                for student in self.students
                if student.department.lower() == department.lower()
            ]
            UI.table(students)
        elif choice == 2:
            excellent = []
            good = []
            average = []
            needs_improvement = []
            for student in self.students:
                if student.cgpa >= 9:
                    excellent.append(student)
                elif student.cgpa >= 8:
                    good.append(student)
                elif student.cgpa >= 7:
                    average.append(student)
                else:
                    needs_improvement.append(student)
            print("\n========== EXCELLENT ==========")
            UI.table(excellent)
            print("\n========== GOOD ==========")
            UI.table(good)
            print("\n========== AVERAGE ==========")
            UI.table(average)
            print("\n===== NEEDS IMPROVEMENT =====")
            UI.table(needs_improvement)
        elif choice == 3:
            year = InputManager.year()
            students = [
                student
                for student in self.students
                if student.year.upper() == year.upper()
            ]
            UI.table(students)
        elif choice == 4:
            placement = InputManager.yes_no(
                "Placement Eligible (Yes/No)"
            )
            students = [
                student
                for student in self.students
                if student.placement_eligible.lower() ==
                placement.lower()
            ]
            UI.table(students)
        elif choice == 5:
            scholarship = InputManager.yes_no(
                "Scholarship (Yes/No)"
            )
            students = [
                student
                for student in self.students
                if student.scholarship.lower() ==
                scholarship.lower()
            ]
            UI.table(students)
        UI.pause()
    @back_handler
    def calculate_cgpa(self):
        UI.title("Calculate CGPA")
        marks = InputManager.text(
            "Enter Marks (Space/Comma Separated)"
        )
        marks = marks.replace(",", " ").split()
        try:
            marks = [float(mark) for mark in marks]
        except ValueError:
            UI.error("Invalid Marks Entered.")
            UI.pause()
            return
        if len(marks) == 0:
            UI.error("No Marks Entered.")
            UI.pause()
            return
        if any(mark < 0 or mark > 100 for mark in marks):
            UI.error("Marks should be between 0 and 100.")
            UI.pause()
            return
        average = sum(marks) / len(marks)
        cgpa = round(average / 10, 2)
        UI.line()
        print(f"Subjects        : {len(marks)}")
        print(f"Average Marks   : {average:.2f}")
        print(f"Calculated CGPA : {cgpa:.2f}")
        if cgpa >= 9:
            print("Performance     : Excellent")
        elif cgpa >= 8:
            print("Performance     : Good")
        elif cgpa >= 7:
            print("Performance     : Average")
        else:
            print("Performance     : Needs Improvement")
        UI.line()
        UI.pause()
    @back_handler
    def performance_analysis(self):
        UI.title("Performance Analysis")
        self.refresh()
        student_id = InputManager.text(
            "Enter Student ID"
        )
        student = self.find_student(student_id)
        if student is None:
            UI.error("Student Not Found.")
            UI.pause()
            return
        UI.student_card(student)
        print("\n========== PERFORMANCE REPORT ==========\n")
        print(f"Student Name        : {student.name}")
        print(f"Department          : {student.department}")
        print(f"Year                : {student.year}")
        print(f"CGPA                : {student.cgpa:.2f}")
        print(f"Average Marks       : {student.average_marks:.2f}")
        print(f"Attendance          : {student.attendance}")
        print(f"Scholarship         : {student.scholarship}")
        print(f"Placement Eligible  : {student.placement_eligible}")
        if student.cgpa >= 9:
            performance = "Excellent ⭐⭐⭐"
        elif student.cgpa >= 8:
            performance = "Good ⭐⭐"
        elif student.cgpa >= 7:
            performance = "Average ⭐"
        else:
            performance = "Needs Improvement"
        print(f"\nOverall Performance : {performance}")
        print("\nSuggestions")
        if student.cgpa < 8:
            print("- Improve academic performance.")
        if student.attendance_percent < 90:
            print("- Increase attendance.")
        if not student.has_scholarship:
            print("- Eligible to apply for scholarships after improving CGPA.")
        if not student.is_placement_ready:
            print("- Improve skills for placement eligibility.")
        if (
            student.cgpa >= 9
            and student.attendance_percent >= 95
            and student.is_placement_ready
        ):
            print("- Ready for premium opportunities.")
            print("- Eligible for hackathons.")
            print("- Recommended for internships.")
            print("- Strong placement profile.")
        UI.line()
        UI.pause()
    @back_handler
    def statistics(self):
        UI.title("Student Statistics")
        self.refresh()
        if len(self.students) == 0:
            UI.warning("No Student Records Found.")
            UI.pause()
            return
        stats = self.analytics.statistics(self.students)
        print("\n========== OVERALL STATISTICS ==========\n")
        print(f"Total Students          : {stats['Total Students']}")
        print(f"Highest CGPA            : {stats['Highest CGPA']}")
        print(f"Lowest CGPA             : {stats['Lowest CGPA']}")
        print(f"Average CGPA            : {stats['Average CGPA']}")
        print(f"Average Attendance      : {stats['Average Attendance']}%")
        print(f"Scholarship Holders     : {stats['Scholarship Holders']}")
        print(f"Placement Eligible      : {stats['Placement Eligible']}")
        print("\n========== DEPARTMENT WISE ==========\n")
        departments = self.analytics.department_statistics(
            self.students
        )
        for department, count in departments.items():
            print(f"{department:<10} : {count}")
        print("\n========== TOP 5 STUDENTS ==========\n")
        top_students = self.analytics.top_students(
            self.students,
            5
        )
        rank = 1
        for student in top_students:
            print(
                f"{rank}. "
                f"{student.name:<20}"
                f"CGPA : {student.cgpa:.2f}"
            )
            rank += 1
        print("\n========== TOP SKILLS ==========\n")
        skills = self.analytics.skill_statistics(
            self.students
        )
        for skill, count in sorted(
            skills.items(),
            key=lambda x: x[1],
            reverse=True
        )[:10]:
            print(f"{skill:<20} : {count}")
        print("\n========== PLACEMENT READINESS ==========\n")
        total_students = len(self.students)
        ready = stats["Placement Eligible"]
        not_ready = total_students - ready
        ready_percent = round((ready / total_students) * 100, 2)
        not_ready_percent = round((not_ready / total_students) * 100, 2)
        print(f"Ready                 : {ready}")
        print(f"Needs Improvement     : {not_ready}")
        print(f"\nPlacement Readiness : {ready_percent}%")
        bars = int(ready_percent // 5)
        print("[" + "█" * bars + "░" * (20 - bars) + "]")
        UI.line()
        UI.pause()
    @back_handler
    def student_recommendation(self):
        UI.title("Student Recommendation")
        self.refresh()
        print("\nRecommendation Based On")
        print("Examples:")
        print("Python")
        print("Java")
        print("Machine Learning")
        print("AI")
        print("Hackathon")
        print("Google AI")
        print("Oracle Java")
        keyword = InputManager.text(
            "Enter Keyword"
        )
        self.recommendation.recommend(
            self.students,
            keyword
        )
        UI.pause()
    @back_handler
    def event_recommendation(self):
        UI.title("Event Recommendation")
        self.refresh()
        events = {
            1: "Smart India Hackathon",
            2: "Coding Contest",
            3: "Project Expo",
            4: "Paper Presentation",
            5: "AI Symposium",
            6: "Placement Drive"
        }
        print("\nAvailable Events\n")
        for key, value in events.items():
            print(f"{key}. {value}")
        choice = InputManager.menu(6)
        event = events[choice]
        recommended = self.event.recommend(
            self.students,
            event
        )
        print(f"\n========== {event.upper()} ==========\n")
        if len(recommended) == 0:
            UI.warning("No Students Recommended.")
            UI.pause()
            return
        UI.table(recommended)
        print(f"\nTotal Recommended : {len(recommended)}")
        UI.pause()