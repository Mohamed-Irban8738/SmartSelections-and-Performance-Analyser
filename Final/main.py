from controllers.monitor import Monitor
from utils.input_manager import InputManager
from utils.ui import UI
from utils.decorators import back_handler
@back_handler
def student_management(monitor):
    while True:
        UI.title("Student Management")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("0. Back")
        choice = InputManager.menu(4)
        if choice == 1:
            monitor.add_student()
        elif choice == 2:
            monitor.view_students()
        elif choice == 3:
            monitor.update_student()
        elif choice == 4:
            monitor.delete_student()
@back_handler
def search_filter(monitor):
    while True:
        UI.title("Search & Filter")
        print("1. Search Student")
        print("2. Filter Students")
        print("3. Group Students")
        print("0. Back")
        choice = InputManager.menu(3)
        if choice == 1:
            monitor.search_student()
        elif choice == 2:
            monitor.filter_students()
        elif choice == 3:
            monitor.group_students()
@back_handler
def analytics_menu(monitor):
    while True:
        UI.title("Analytics")
        print("1. Performance Analysis")
        print("2. Calculate CGPA")
        print("3. Statistics")
        print("0. Back")
        choice = InputManager.menu(3)
        if choice == 1:
            monitor.performance_analysis()
        elif choice == 2:
            monitor.calculate_cgpa()
        elif choice == 3:
            monitor.statistics()
@back_handler
def recommendation_menu(monitor):
    while True:
        UI.title("Recommendation")
        print("1. Student Recommendation")
        print("2. Event Recommendation")
        print("0. Back")
        choice = InputManager.menu(2)
        if choice == 1:
            monitor.student_recommendation()
        elif choice == 2:
            monitor.event_recommendation()
def main():
    monitor = Monitor()
    while True:
        UI.title("SmartSelections and Performance Analyser")
        print("1. Student Management")
        print("2. Search & Filter")
        print("3. Analytics")
        print("4. Recommendation")
        print("5. Exit")
        choice = InputManager.menu(5)
        if choice == 1:
            student_management(monitor)
        elif choice == 2:
            search_filter(monitor)
        elif choice == 3:
            analytics_menu(monitor)
        elif choice == 4:
            recommendation_menu(monitor)
        elif choice == 5:
            UI.success("Thank you for using SmartSelections and Performance Analyser.")
            break
if __name__ == "__main__":
    main()