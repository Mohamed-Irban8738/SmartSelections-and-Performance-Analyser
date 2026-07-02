from collections import Counter
class Analytics:
    def statistics(self, students):
        stats = {}
        if len(students) == 0:
            return stats
        cgpas = [student.cgpa for student in students]
        attendance = [
            student.attendance_percent
            for student in students
        ]
        stats["Total Students"] = len(students)
        stats["Highest CGPA"] = max(cgpas)
        stats["Lowest CGPA"] = min(cgpas)
        stats["Average CGPA"] = round(
            sum(cgpas)/len(cgpas),2
        )
        stats["Average Attendance"] = round(
            sum(attendance)/len(attendance),2
        )
        stats["Placement Eligible"] = sum(
            student.is_placement_ready
            for student in students
        )
        stats["Scholarship Holders"] = sum(
            student.has_scholarship
            for student in students
        )
        return stats
    def department_statistics(self, students):
        counter = Counter()
        for student in students:
            counter[student.department] += 1
        return counter
    def skill_statistics(self, students):
        counter = Counter()
        for student in students:
            for skill in student.skills_list:
                counter[skill] += 1
        return counter
    def top_students(self, students, limit=10):
        return sorted(
            students,
            key=lambda s: s.cgpa,
            reverse=True
        )[:limit]
    def low_students(self, students, limit=10):
        return sorted(
            students,
            key=lambda s: s.cgpa
        )[:limit]