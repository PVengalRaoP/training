# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a ** b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def main():
    while True:
        print("\nSimple CLI Calculator")
        print("======================")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Select an option (1/2/3/4/5): ")

        if choice == "5":
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ["1", "2", "3", "4"]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == "1":
                print(f"Result: {a} + {b} = {add(a, b)}")
            elif choice == "2":
                print(f"Result: {a} - {b} = {subtract(a, b)}")
            elif choice == "3":
                print(f"Result: {a} x {b} = {multiply(a, b)}")
            elif choice == "4":
                if b == 0:
                    print("Error: Cannot divide by zero!")
                else:
                    print(f"Result: {a} / {b} = {divide(a, b)}")
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
