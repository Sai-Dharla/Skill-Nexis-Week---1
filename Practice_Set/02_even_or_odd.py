def check_even_odd(number):
    """Checks if a given number is even or odd."""
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
def main():
    print("--- Even or Odd Checker ---")
    try:
        num = int(input("Enter an integer: "))
        result = check_even_odd(num)
        print(f"The number {num} is {result}.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
if __name__ == "__main__":
    main()