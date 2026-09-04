import math

def calculate_area(radius):
    """Calculates the area of a circle given its radius."""
    # Formula for the area of a circle is π * r^2
    return math.pi * (radius ** 2)
def main():
    print("--- Area of a Circle Calculator ---")
    try:
        # Get radius input from the user
        radius = float(input("Enter the radius of the circle: "))
        if radius < 0:
            print("Radius cannot be negative. Please enter a valid number.")
        else:
            area = calculate_area(radius)
            # Print the result rounded to 2 decimal places
            print(f"The area of a circle with radius {radius} is: {area:.2f}")
    except ValueError:
        print("Invalid input! Please enter a numerical value.")
if __name__ == "__main__":
    main()