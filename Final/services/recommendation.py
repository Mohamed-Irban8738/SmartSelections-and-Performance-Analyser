from utils.ui import UI
class RecommendationEngine:
    def recommend(self, students, keyword):
        keyword = keyword.lower()
        recommendations = []
        for student in students:
            score = 0
            for skill in student.skills_list:
                if keyword in skill:
                    score += 4
            for cert in student.certificate_list:
                if keyword in cert:
                    score += 3
            for event in student.event_list:
                if keyword in event:
                    score += 2
            if keyword in student.department.lower():
                score += 2
            if student.cgpa >= 9:
                score += 3
            elif student.cgpa >= 8:
                score += 2
            if student.attendance_percent >= 95:
                score += 2
            if student.has_scholarship:
                score += 1
            if student.is_placement_ready:
                score += 1
            if score > 0:
                recommendations.append((score, student))
        recommendations.sort(
            reverse=True,
            key=lambda x: x[0]
        )
        if len(recommendations) == 0:
            UI.warning("No Matching Students Found.")
            return
        UI.line()
        print(
            f"{'Rank':<6}"
            f"{'Score':<8}"
            f"{'Name':<25}"
            f"{'CGPA'}"
        )
        UI.line()
        rank = 1
        for score, student in recommendations:
            print(
                f"{rank:<6}"
                f"{score:<8}"
                f"{student.name:<25}"
                f"{student.cgpa}"
            )
            rank += 1
        UI.line()