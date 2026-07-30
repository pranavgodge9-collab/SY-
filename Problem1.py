def student_details(name, age):
    print("Required Arguments")
    print("Name :", name)
    print("Age  :", age)
    print()

def employee_details(name, department, salary):
    print("Keyword Arguments")
    print("Name       :", name)
    print("Department :", department)
    print("Salary     :", salary)
    print()


def calculate_bill(item, quantity=1, price=100):
    total = quantity * price
    print("Default Arguments")
    print("Item     :", item)
    print("Quantity :", quantity)
    print("Price    :", price)
    print("Total    :", total)
    print()


def find_sum(*numbers):
    print("Variable-Length Arguments")
    print("Numbers :", numbers)
    print("Sum     :", sum(numbers))
    print()


def display_information(**details):
    print("Variable-Length Keyword Arguments")
    for key, value in details.items():
        print(f"{key} : {value}")
    print()


student_details("Pranav", 20)

employee_details(salary=50000, department="IT", name="Rahul")

calculate_bill("Laptop")
calculate_bill("Mobile", 2, 15000)

find_sum(10, 20, 30)
find_sum(5, 10, 15, 20, 25)

display_information(
    Name="Amit",
    Age=25,
    City="Pune",
    Profession="Engineer"
)