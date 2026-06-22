pin = "1234"

try:
    with open("balance.txt", "r") as file:
        balance = float(file.read())
except FileNotFoundError:
    balance = 100

attempts = 3

while attempts > 0:
    entered_pin = input("Enter PIN: ")

    if entered_pin == pin:
        print("Login Successful!")
        break

    attempts -= 1
    print(f"Wrong PIN! Attempts left: {attempts}")

if attempts == 0:
    print("Too many wrong attempts!")
    exit()

while True:

    print("\n===== ATM =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Check Balance
    if choice == "1":
        print(f"Current Balance: {balance} Tk")

    # Deposit
    elif choice == "2":
        amount = float(input("Enter deposit amount: "))

        balance += amount

        with open("balance.txt", "w") as file:
            file.write(str(balance))

        with open("history.txt", "a") as file:
            file.write(f"Deposited {amount} Tk\n")

        print("Deposit successful!")

    # Withdraw
    elif choice == "3":
        amount = float(input("Enter withdraw amount: "))

        if amount <= balance:

            balance -= amount

            with open("balance.txt", "w") as file:
                file.write(str(balance))

            with open("history.txt", "a") as file:
                file.write(f"Withdrawn {amount} Tk\n")

            print("Withdraw successful!")

        else:
            print("Insufficient balance!")

    # Transaction History
    elif choice == "4":

        try:
            with open("history.txt", "r") as file:
                history = file.read()

                if history:
                    print("\n===== TRANSACTION HISTORY =====")
                    print(history)
                else:
                    print("No transactions yet.")

        except FileNotFoundError:
            print("No transactions yet.")

    # Exit
    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
