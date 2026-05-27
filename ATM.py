blance = 1000

while True:
    print("\n===== ATM MENU ======")
    print("1. Check Blance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Inter your choice: ")

    if choice == 1:
        print(f"Curent Blance: {blance} Tk")
    elif choice == 2:
        amount = float(input("Enter your deposite amout: "))
        if amount > 0:
            blance += amount
            print(f"{amount} tk diposited successfully")
    elif choice == 3:
        amount = float(input("Enter withdraw amount: "))
        if amount <= blance:
            blance -= amount
            print(f"{amount} Tk withdraw successfully.")
        else:
            print("Insufficient balance.")
    elif choice == 4:
        print("Thank you for using the ATM.")
        break
    else:
        print("Invalid choice.")

