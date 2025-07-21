class Student:
    def __init__(self, name, age):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Age must be a positive integer.")
            
        self.name = name
        self.age = age
        self.grades = {}

    def add_grade(self, subject, marks):
        if not isinstance(marks, (int, float)) or not (0 <= marks <= 100):
             raise ValueError("Marks must be a number between 0 and 100.")
        self.grades[subject] = marks
        print(f"Added grade for {subject}: {marks}")

    def calculate_average(self):
        if not self.grades:
            return 0
        total_marks = sum(self.grades.values())
        return total_marks / len(self.grades)

    def assign_grade(self):
        average = self.calculate_average()
        if average >= 80:
            return 'A'
        elif 60 <= average < 80:
            return 'B'
        elif 40 <= average < 60:
            return 'C'
        else:
            return 'F'

    def apply_bonus(self, bonus_func):
        for subject, marks in self.grades.items():
            self.grades[subject] = min(100, bonus_func(marks))
        print("Bonus marks applied successfully.")

    def generate_report(self):
        average = self.calculate_average()
        letter_grade = self.assign_grade()
        
        report = f"--- Student Report Card ---\n"
        report += f"Name: {self.name}\n"
        report += f"Age: {self.age}\n"
        report += "---------------------------\n"
        report += "Subjects & Marks:\n"
        if not self.grades:
            report += "  No grades available.\n"
        else:
            for subject, marks in self.grades.items():
                report += f"  - {subject}: {marks}\n"
        report += "---------------------------\n"
        report += f"Average: {average:.2f}\n"
        report += f"Final Grade: {letter_grade}\n"
        report += "---------------------------\n"
        return report

    def save_to_file(self, filename=None):
        if filename is None:
            filename = f"{self.name.lower().replace(' ', '_')}_report.txt"
        
        report = self.generate_report()
        try:
            with open(filename, 'w') as f:
                f.write(report)
            print(f"Report saved successfully to {filename}")
            return filename
        except IOError as e:
            print(f"Error: Could not save report to file {filename}. Reason: {e}")
            return None

    @staticmethod
    def load_from_file(filename):
        try:
            with open(filename, 'r') as f:
                print(f"\n--- Reading Report from {filename} ---")
                print(f.read())
        except IOError as e:
            print(f"Error: Could not read report from file {filename}. Reason: {e}")

def main():
    print("--- Student Report Card Generator ---")
    
    try:
        student_name = input("Enter student's name: ")
        student_age = int(input("Enter student's age: "))
        
        student = Student(student_name, student_age)

        math_marks = float(input("Enter marks for Math: "))
        student.add_grade("Math", math_marks)
        
        english_marks = float(input("Enter marks for English: "))
        student.add_grade("English", english_marks)
        
        urdu_marks = float(input("Enter marks for Urdu: "))
        student.add_grade("Urdu", urdu_marks)

        apply_bonus_choice = input("Do you want to apply 5 bonus marks to all subjects? (yes/no): ")
        
        if apply_bonus_choice == 'yes':
            student.apply_bonus(lambda marks: marks + 5)
            
        print("\n" + student.generate_report())

        report_filename = student.save_to_file()
        
    

    except ValueError as ve:
        print(f"\nInput Error: {ve}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
