from datetime import datetime
from functools import wraps


is_logged_in = True      


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if is_logged_in:
            return func(*args, **kwargs)
        else:
            print(" Access Denied! Please login first.")
    return wrapper


@login_required
def view_profile():
    print(" Welcome! You are viewing your profile.")


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\nFunction Name : {func.__name__}")
        print("Called At     :", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
        return func(*args, **kwargs)
    return wrapper


@logger
def greet(name):
    print(f"Hello, {name}!")


def validate_positive(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        for arg in args:
            if not isinstance(arg, int) or arg <= 0:
                print(" Error: All arguments must be positive integers.")
                return

        for value in kwargs.values():
            if not isinstance(value, int) or value <= 0:
                print(" Error: All arguments must be positive integers.")
                return

        return func(*args, **kwargs)
    return wrapper


@validate_positive
def multiply(a, b):
    print("Multiplication =", a * b)


def call_counter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"{func.__name__} has been called {wrapper.count} time(s).")
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper


@call_counter
def say_hello():
    print("Hello Everyone!")


print("Task 1: Login Authentication")
view_profile()

print("\nTask 2: Function Call Logger")
greet("Pranav")

print("\nTask 3: Input Validation")
multiply(10, 5)
multiply(-2, 5)
multiply(4, "A")

print("\nTask 4: Function Call Counter")
say_hello()
say_hello()
say_hello()