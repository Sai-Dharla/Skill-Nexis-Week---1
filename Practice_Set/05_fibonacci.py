def print_fibonacci(n):
    """Prints the Fibonacci sequence up to n terms."""
    # First two terms of Fibonacci sequence
    a, b = 0, 1
    count = 0
    
    if n <= 0:
        print("Please enter a positive integer.")
    elif n == 1:
        print("Fibonacci sequence:")
        print(a)
    else:
        print("Fibonacci sequence:")
        while count < n:
            print(a, end=" ")
            # Update values
            next_term = a + b
            a = b
            b = next_term
            count += 1
        print() # For a new line at the end

def main():
    print("--- Fibonacci Sequence Generator ---")
    try:
        n = int(input("Enter the number of terms: "))
        print_fibonacci(n)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()

