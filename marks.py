# Simple Student Marks Management System

class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def add_mark(self, mark):
        self.marks.append(mark)

    def average(self):
        return sum(self.marks) / len(self.marks) if self.marks else 0

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return "A+"
        elif avg >= 75:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 40:
            return "C"
        else:
            return "Fail"

# ---- main program ----
students = []

for i in range(3):  # take 3 students for demo
    name = input(f"Enter name of student {i+1}: ")
    s = Student(name)

    for j in range(3):  # 3 subjects
        mark = int(input(f"Enter mark {j+1} for {name}: "))
        s.add_mark(mark)

    students.append(s)

print("\n--- Report Card ---")
for s in students:
    print(f"Name: {s.name}, Avg: {s.average():.2f}, Grade: {s.grade()}")
