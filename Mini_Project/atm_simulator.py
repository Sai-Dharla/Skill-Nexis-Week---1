def check_balance(balance):
    print("Current balance:", balance)
def deposit_money(balance):
    amount = float(input("Enter deposit amount: "))
    if amount > 0:
        balance += amount
        print("Deposit successful.")
        print("Updated balance:", balance)
    else:
        print("Invalid deposit amount.")
    return balance
def withdraw_money(balance):
    amount = float(input("Enter withdrawal amount: "))
    if amount <= 0:
        print("Invalid withdrawal amount.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print("Withdrawal successful.")
        print("Updated balance:", balance)
    return balance
correct_pin = "1234"
balance = 1000.0
print("===== Welcome to Simple ATM =====")
entered_pin = input("Enter your PIN: ")
if entered_pin == correct_pin:
    print("Login successful!")
    while True:
        print("\n===== ATM Menu =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            check_balance(balance)
        elif choice == "2":
            balance = deposit_money(balance)
        elif choice == "3":
            balance = withdraw_money(balance)
        elif choice == "4":
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid choice. Please select 1-4.")
else:
    print("Incorrect PIN. Access denied.")