class Student:
    def __init__(
        self,
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
        placement_eligible
    ):
        self.id = student_id
        self.name = name
        self.department = department
        self.year = year
        self.cgpa = float(cgpa)
        self.skills = skills
        self.certifications = certifications
        self.previous_events = previous_events
        self.attendance = attendance
        self.average_marks = float(average_marks)
        self.scholarship = scholarship
        self.placement_eligible = placement_eligible
    def __str__(self):
        return (
            f"{self.id} | "
            f"{self.name} | "
            f"{self.department} | "
            f"{self.cgpa}"
        )
    def to_dict(self):
        return {
            "ID": self.id,
            "Name": self.name,
            "Department": self.department,
            "Year": self.year,
            "CGPA": self.cgpa,
            "Skills": self.skills,
            "Certifications": self.certifications,
            "Previous_Events": self.previous_events,
            "Attendance": self.attendance,
            "Average_Marks": self.average_marks,
            "Scholarship": self.scholarship,
            "Placement_Eligible": self.placement_eligible
        }
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["ID"],
            data["Name"],
            data["Department"],
            data["Year"],
            data["CGPA"],
            data["Skills"],
            data["Certifications"],
            data["Previous_Events"],
            data["Attendance"],
            data["Average_Marks"],
            data["Scholarship"],
            data["Placement_Eligible"]
        )
    def update(self, field, value):
        if field == "cgpa":
            self.cgpa = float(value)
        elif field == "average_marks":
            self.average_marks = float(value)
        else:
            setattr(self, field, value)
    @property
    def performance(self):
        if self.cgpa >= 9:
            return "Excellent"
        elif self.cgpa >= 8:
            return "Good"
        elif self.cgpa >= 7:
            return "Average"
        else:
            return "Needs Improvement"
    @property
    def is_placement_ready(self):
        return self.placement_eligible.lower() == "yes"
    @property
    def has_scholarship(self):
        return self.scholarship.lower() == "yes"
    @property
    def attendance_percent(self):
        return float(self.attendance.replace("%", ""))
    @property
    def skills_list(self):
        return [
            skill.strip().lower()
            for skill in self.skills.split(",")
        ]
    @property
    def event_list(self):
        return [
            event.strip().lower()
            for event in self.previous_events.split(",")
        ]
    @property
    def certificate_list(self):
        return [
            cert.strip().lower()
            for cert in self.certifications.split(",")
        ]