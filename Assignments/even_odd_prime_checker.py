def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
def check_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
number = int(input("Enter a number: "))
print("Number is:", check_even_odd(number))
if check_prime(number):
    print("Number is Prime")
else:
    print("Number is Not Prime")