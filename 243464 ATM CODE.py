userData = {}  # Dictionary to store user account details (name, PIN, balance).

maxAttempts = 3

# Time Taken to finish: 10 mins
# Function for ensuring user inputs are between a certain domain
def getNumberInput(prompt, minValue, maxValue):
    while True:
        try:
            value = int(input(prompt))
            if minValue <= value <= maxValue:
                return value
            else:
                print(f"Value must be between {minValue} and {maxValue}.")
        except ValueError:
            print("Invalid input! Please input a number.")

# Time Taken to finish: 2 days
# Function for ensuring user inputs are valid by length
def getStringInput(prompt, length, numeric=True):
    while True:
        value = input(prompt).strip()
        if numeric:
            if value.isdigit() and len(value) == length:
                return value
            print(f"Invalid! Please input a {length}-digit number.")
        else:
            if value.isalpha() and len(value) > 0:
                return value
            print("Invalid! Please input a valid name (letters only).")

# Time Taken to finish: 25 mins
# Function for handling user account creation
def createAccount():
    global userData
    print("Create a New Account")
    while True:
        accountno = getStringInput("Enter a new account number (10 digits): ", 10, numeric=True)
        if accountno in userData:
            print("Account number already exists. Please choose another one.")
        else:
            name = getStringInput("Enter your name (letters only): ", 0, numeric=False)
            pin = getStringInput("Enter a new PIN (5 digits): ", 5, numeric=True)
            initialBalance = getNumberInput("Enter initial deposit amount (Min: 1000): ", 1000, 1000000)
            userData[accountno] = {"name": name, "pin": pin, "balance": initialBalance}
            print(f"Account successfully created for {name}!")
            break

# Time Taken to finish: 5 mins
def verifyCredentials(accountno, pin):
    return accountno in userData and userData[accountno]["pin"] == pin

# Time taken to finish: 1 day
# Function for handling the user login process
def login():
    attempts = 0
    while attempts < maxAttempts:
        accountno = getStringInput("Enter your account number: ", 10, numeric=True)
        pin = getStringInput("Enter your PIN: ", 5, numeric=True)

        if verifyCredentials(accountno, pin):
            print(f"Welcome, {userData[accountno]['name']}!")
            BackToMain(accountno)
            return
        else:
            attempts += 1
            print(f"Invalid credentials. You have {maxAttempts - attempts} attempt(s) left.")

    print("Too many failed attempts. Exiting.")
    exit()

# Time Taken to finish: 15 mins
# Function for handling the deposits, if deposit criteria has been met
def deposit(accountno):
    while True:
        depositAmount = getNumberInput("Input an amount to deposit (Min: 200, Max: 10000): ", 200, 10000)
        if depositAmount is not None:
            print("Transaction Processing...")
            userData[accountno]["balance"] += depositAmount
            print(f"Deposit Completed. Your New Balance is {userData[accountno]['balance']}")
            break


def checkBalance(accountno):
    print(f"Your account balance is: {userData[accountno]['balance']} Naira")

# Time Taken to finish: 1 week
# Function for handling the withdrawal choices
def withdraw(accountno):
    options = {
        "1": 1000,
        "2": 2000,
        "3": 5000,
        "4": 10000,
        "5": 20000
    }
    while True:
        print("Withdrawal Menu")
        for key, value in options.items():
            print(f" {key}- N {value} ")
        print(" 6- Cancel Transaction")
        withdrawChoice = input("Select an amount to withdraw: ")
        if withdrawChoice in options:
            withdrawAmount = options[withdrawChoice]
            withdrawalProcess(accountno, withdrawAmount)
            break
        elif withdrawChoice == "6":
            print("Transaction Cancelled")
            print(f"Your Balance is {userData[accountno]['balance']}")
            break
        else:
            print("Invalid input! Please select a number between 1 and 6")

# Time Taken to finish: 4 days
# Function for handling the withdrawal process
def withdrawalProcess(accountno, withdrawAmount):
    print("Transaction Processing...")
    if userData[accountno]["balance"] >= withdrawAmount:
        userData[accountno]["balance"] -= withdrawAmount
        print(f"Withdrawing N {withdrawAmount}...")
        print("Transaction Complete! Please take your cash.")
    else:
        print("Insufficient Funds. Please fund your account.")

# Time Taken to finish: 2 days
# Main menu function
def mainMenu():
    print("Main Menu")
    print("    1 - View my balance")
    print("    2 - Withdraw cash")
    print("    3 - Deposit funds")
    print("    4 - Logout")
    print("    5 - Exit")
    return input("Enter a choice (1-5): ")

# Time Taken to finish: 2 days
# Function for returning back to main menu after transactions
def BackToMain(accountno):
    while True:
        TransactionChoice = mainMenu()
        if TransactionChoice == "1":
            checkBalance(accountno)
        elif TransactionChoice == "2":
            withdraw(accountno)
        elif TransactionChoice == "3":
            deposit(accountno)
        elif TransactionChoice == "4":
            print("Logging out...")
            LandingScreen()  # Logs out the user by returning to the landing screen
            return
        elif TransactionChoice == "5":
            print("Thank you for choosing ABC.")
            exit()
        else:
            print("Invalid input! Please Try Again.")

        if not ConfirmNewTransaction():
            exit()

# Time Taken to finish: 6 hours
# Function for confirming whether to carry out new transaction or not
def ConfirmNewTransaction():
    returnMenu = input("Would you like to carry out another transaction? (Y/N): ").strip().upper()
    while returnMenu not in ["Y", "N"]:
        print("Invalid input. Please select (Y)es or (N)o.")
        returnMenu = input("Would you like to carry out another transaction? (Y/N): ").strip().upper()
    if returnMenu == "N":
        print("Thank you for choosing ABC")
        return False
    return True

# Time Taken to finish: 2 hours
# Function for the initial, welcome screen
def LandingScreen():
    print("Welcome to ABC Bank")
    while True:
        print("1 - Login")
        print("2 - Create New Account")
        choice = input("Choose an option (1 or 2): ").strip()

        if choice == "1":
            login()
        elif choice == "2":
            createAccount()
        else:
            print("Invalid option. Please select 1 or 2.")


# Start the program.
LandingScreen()
