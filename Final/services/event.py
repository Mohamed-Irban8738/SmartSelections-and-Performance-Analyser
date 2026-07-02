class EventService:
    def recommend(self, students, event):
        event = event.lower()
        selected = []
        for student in students:
            if event == "smart india hackathon":
                if (
                    student.cgpa >= 8.5
                    and student.attendance_percent >= 90
                    and (
                        "python" in student.skills_list
                        or
                        "ml" in student.skills_list
                        or
                        "genai" in student.skills_list
                        or
                        "ai" in student.skills_list
                    )
                ):
                    selected.append(student)
            elif event == "coding contest":
                if (
                    "python" in student.skills_list
                    or
                    "java" in student.skills_list
                    or
                    "c++" in student.skills_list
                    or
                    "dsa" in student.skills_list
                ):
                    selected.append(student)
            elif event == "project expo":
                if (
                    "iot" in student.skills_list
                    or
                    "embedded c" in student.skills_list
                    or
                    "opencv" in student.skills_list
                    or
                    "robotics" in student.skills_list
                ):
                    selected.append(student)
            elif event == "paper presentation":
                if student.cgpa >= 8:
                    selected.append(student)
            elif event == "ai symposium":
                if (
                    "python" in student.skills_list
                    or
                    "ml" in student.skills_list
                    or
                    "deep learning" in student.skills_list
                    or
                    "llm" in student.skills_list
                    or
                    "genai" in student.skills_list
                ):
                    selected.append(student)
            elif event == "placement drive":
                if student.is_placement_ready:
                    selected.append(student)
        return selected