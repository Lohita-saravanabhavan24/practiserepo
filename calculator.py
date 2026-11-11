def add(first, second):
    return first + second


def subtract(first, second):
    return first - second


def multiply(first, second):
    return first * second


def divide(first, second):
    if second == 0:
        raise ValueError("Cannot divide by zero.")
    return first / second


def main():
    operations = {
        "1": ("Add", add),
        "2": ("Subtract", subtract),
        "3": ("Multiply", multiply),
        "4": ("Divide", divide),
    }

    while True:
        print("\nCalculator")
        for choice, (name, _) in operations.items():
            print(f"{choice}. {name}")
        print("5. Quit")

        choice = input("Choose an option: ").strip()
        if choice == "5":
            print("Goodbye!")
            break
        if choice not in operations:
            print("Invalid choice. Please select an option from 1 to 5.")
            continue

        try:
            first = float(input("Enter the first number: "))
            second = float(input("Enter the second number: "))
            name, operation = operations[choice]
            result = operation(first, second)
        except ValueError as error:
            print(f"Invalid input: {error}")
            continue

        print(f"Result: {result}")


if __name__ == "__main__":
    main()