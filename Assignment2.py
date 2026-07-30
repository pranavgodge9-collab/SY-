from datetime import datetime

def border(func):
    def wrapper(*args, **kwargs):
        report = func(*args, **kwargs)
        line = "*" * 50
        return f"{line}\n{report}\n{line}"
    return wrapper


def footer(func):
    def wrapper(*args, **kwargs):
        report = func(*args, **kwargs)
        return f"{report}\nEnd of Report"
    return wrapper


def uppercase(func):
    def wrapper(*args, **kwargs):
        report = func(*args, **kwargs)
        return report.upper()
    return wrapper


def add_date(func):
    def wrapper(*args, **kwargs):
        report = func(*args, **kwargs)
        today = datetime.now().strftime("%d/%m/%Y")
        return f"{report}\nGenerated On: {today}"
    return wrapper

class Report:

    def __init__(self, title, author, content, date=None):
        self.title = title
        self.author = author
        self.content = content
        self.date = date if date else datetime.now().strftime("%d/%m/%Y")

   
    @classmethod
    def student_template(cls):
        content = (
            "Student Name : Pranav\n"
            "Marks        : 95\n"
            "Grade        : A"
        )
        return cls("Student Report", "Sushma", content)

    @classmethod
    def employee_template(cls):
        content = (
            "Employee Name : Rahul\n"
            "Department    : IT\n"
            "Salary        : 70000"
        )
        return cls("Employee Report", "Manager", content)

    @classmethod
    def sales_template(cls):
        content = (
            "Product  : Laptop\n"
            "Quantity : 15\n"
            "Revenue  : ₹9,00,000"
        )
        return cls("Sales Report", "Sales Team", content)

    @classmethod
    def attendance_template(cls):
        content = (
            "Employee : Amit\n"
            "Present Days : 26\n"
            "Absent Days  : 2"
        )
        return cls("Attendance Report", "HR", content)


    def __str__(self):
        return (f"Title  : {self.title}\n"
                f"Author : {self.author}\n"
                f"Date   : {self.date}\n\n"
                f"{self.content}")

    def __len__(self):
        return len(str(self))

    def __add__(self, other):
        new_title = self.title + " + " + other.title
        new_author = self.author + " & " + other.author
        new_content = self.content + "\n\n" + other.content
        return Report(new_title, new_author, new_content)

    def __eq__(self, other):
        return self.title == other.title and self.content == other.content



@border
@footer
@add_date
@uppercase
def generate_report(report):
    return str(report)



if __name__ == "__main__":

    student = Report.student_template()
    employee = Report.employee_template()
    sales = Report.sales_template()

    print("\nSTUDENT REPORT")
    print(generate_report(student))

    print("\nEMPLOYEE REPORT")
    print(generate_report(employee))

    print("\nSALES REPORT")
    print(generate_report(sales))

    print("\nLength of Student Report:", len(student))

    combined = student + employee
    print("\nCOMBINED REPORT")
    print(generate_report(combined))

    another_student = Report.student_template()

    print("\nComparison:")
    print("student == another_student :", student == another_student)
    print("student == employee        :", student == employee)