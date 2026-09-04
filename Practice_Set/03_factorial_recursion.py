def factorial(n):
    """Calculates the factorial of a number using recursion."""
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n * factorial(n-1)
    else:
        return n * factorial(n - 1)

def main():
    print("--- Factorial using Recursion ---")
    try:
        num = int(input("Enter a positive integer: "))
        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            result = factorial(num)
            print(f"The factorial of {num} is: {result}")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()

