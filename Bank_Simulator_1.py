def user_details(name, account_number, account_balance):
    print("User details:")
    print(f"Name: {name}")
    print(f"Account Number: {account_number}")
    print(f"Account Balance: {account_balance}")

def deposit(balance):
    amount = int(input("Enter amount to be deposited: "))
    balance += amount
    print(f"Balance after deposit: ${balance}")
    return balance

def withdraw(balance):
    debit = int(input("Enter the amount to withdraw: "))
    if debit > balance:
        print("You do not have enough balance to withdraw. Enter less amount! ")
    else:
        balance -= debit
        print(f"Balance after withdrawl: ${balance}")
    return balance

#User inputs
name = input("Enter Name: ")
account_number = int(input("Enter Account Number: "))
account_balance = int(input("Enter the Starting Balance: "))

user_details(name, account_number, account_balance)
account_balance = deposit(account_balance)
account_balance = withdraw(account_balance)
