import pickle
import os
import hashlib
import random
import string

class Bank:
    def __init__(self):
        self.accounts = {}
        self.atm_cards = {}
        self.online_passwords = {}
        self.loans = {}
        self.fixed_deposits = {}

    def create_account(self, name, initial_balance):
        account_number = random.randint(10000, 99999)
        pin = int(input("Set your 4-digit PIN: "))
        password = input("Set your online password: ")
        
        self.accounts[account_number] = {"name": name, "balance": initial_balance}
        self.atm_cards[account_number] = {"pin": pin, "is_blocked": False}
        self.online_passwords[account_number] = password
        self.loans[account_number] = {"amount": 0, "interest_rate": 0.1, "remaining_payments": 0}
        self.fixed_deposits[account_number] = {"amount": 0, "interest_rate": 0.05, "term_months": 0}
        
        print(f"Account created successfully. Your account number is {account_number}.")

    def display_balance(self, account_number):
        if account_number in self.accounts:
            return f"Your balance is: {self.accounts[account_number]['balance']}"
        else:
            return "Account not found."

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]["balance"] += amount
            return f"Deposit successful. New balance: {self.accounts[account_number]['balance']}"
        else:
            return "Account not found."

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number]["balance"] >= amount:
                self.accounts[account_number]["balance"] -= amount
                return f"Withdrawal successful. New balance: {self.accounts[account_number]['balance']}"
            else:
                return "Insufficient funds."
        else:
            return "Account not found."

    def block_card(self, account_number):
        if account_number in self.atm_cards:
            self.atm_cards[account_number]["is_blocked"] = True
            return "Card blocked successfully."
        else:
            return "Account not found."

    def unblock_card(self, account_number):
        if account_number in self.atm_cards:
            self.atm_cards[account_number]["is_blocked"] = False
            return "Card unblocked successfully."
        else:
            return "Account not found."

    def validate_pin(self, account_number, entered_pin):
        if account_number in self.atm_cards:
            if not self.atm_cards[account_number]["is_blocked"] and self.atm_cards[account_number]["pin"] == entered_pin:
                return True
        return False

    def make_online_payment(self, account_number, password, amount):
        if account_number in self.online_passwords:
            if self.online_passwords[account_number] == password:
                if account_number in self.accounts and self.accounts[account_number]["balance"] >= amount:
                    self.accounts[account_number]["balance"] -= amount
                    return f"Online payment successful. New balance: {self.accounts[account_number]['balance']}"
                else:
                    return "Insufficient funds."
            else:
                return "Incorrect online password."
        else:
            return "Account not found."

    def apply_loan(self, account_number, loan_amount, term_months):
        if account_number in self.loans and self.loans[account_number]["remaining_payments"] == 0:
            self.loans[account_number]["amount"] = loan_amount
            self.loans[account_number]["remaining_payments"] = term_months
            return f"Loan approved. You will make {term_months} monthly payments."
        elif self.loans[account_number]["remaining_payments"] > 0:
            return "You already have an active loan."
        else:
            return "Account not found."

    def open_fixed_deposit(self, account_number, deposit_amount, term_months):
        if account_number in self.fixed_deposits and self.fixed_deposits[account_number]["term_months"] == 0:
            self.fixed_deposits[account_number]["amount"] = deposit_amount
            self.fixed_deposits[account_number]["term_months"] = term_months
            return f"Fixed deposit created. It will mature in {term_months} months."
        elif self.fixed_deposits[account_number]["term_months"] > 0:
            return "You already have an active fixed deposit."
        else:
            return "Account not found."

    def deposit_loan_amount(self, account_number):
        if account_number in self.loans and self.loans[account_number]["remaining_payments"] > 0:
            loan_amount = self.loans[account_number]["amount"]
            self.accounts[account_number]["balance"] += loan_amount
            self.loans[account_number]["remaining_payments"] = 0
            self.loans[account_number]["amount"] = 0
            return f"Loan amount deposited. New balance: {self.accounts[account_number]['balance']}"
        else:
            return "No active loans or payments remaining."
    def list_accounts(self):
        for acc_no, account in self.accounts.items():
            print(account)

    def load_accounts(self):
        if os.path.exists("accounts.pkl"):
            with open("accounts.pkl", "rb") as file:
                self.accounts = pickle.load(file)

    def save_accounts(self):
        with open("accounts.pkl", "wb") as file:
            pickle.dump(self.accounts, file)

# Example usage:
bank = Bank()

while True:
    print("\t")
    print("\t\t\t\t**********************")
    print("\t\t\t\tBANK MANAGEMENT SYSTEM")
    print("\t\t\t\t**********************")

    print("\t\t\t\tBrought To You By:")
    print("\t\t\t\tUDIIT BANSAL,")
    print("MAIN MENU")
    print(" 1.Create Account\n2. Display Balance\n3. Deposit\n4. Withdraw\n5. Block Card\n6. Unblock Card\n7. Make Online Payment\n8. Apply for Loan\n9. Open Fixed Deposit\n10. Deposit Loan Amount.\n11. List of Account.\n12. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter your name: ")
        initial_balance = float(input("Enter initial balance: "))
        bank.create_account(name, initial_balance)

    elif choice == 2:
        account_number = int(input("Enter your account number: "))
        print(bank.display_balance(account_number))

    elif choice == 3:
        account_number = int(input("Enter your account number: "))
        amount = float(input("Enter the deposit amount: "))
        print(bank.deposit(account_number, amount))

    elif choice == 4:
        account_number = int(input("Enter your account number: "))
        amount = float(input("Enter the withdrawal amount: "))
        print(bank.withdraw(account_number, amount))

    elif choice == 5:
        account_number = int(input("Enter your account number: "))
        print(bank.block_card(account_number))

    elif choice == 6:
        account_number = int(input("Enter your account number: "))
        print(bank.unblock_card(account_number))

    elif choice == 7:
        account_number = int(input("Enter your account number: "))
        password = input("Enter your online password: ")
        amount = float(input("Enter the payment amount: "))
        print(bank.make_online_payment(account_number, password, amount))

    elif choice == 8:
        account_number = int(input("Enter your account number: "))
        loan_amount = float(input("Enter the loan amount: "))
        term_months = int(input("Enter the loan term in months: "))
        print(bank.apply_loan(account_number, loan_amount, term_months))

    elif choice == 9:
        account_number = int(input("Enter your account number: "))
        deposit_amount = float(input("Enter the deposit amount: "))
        term_months = int(input("Enter the term in months: "))
        print(bank.open_fixed_deposit(account_number, deposit_amount, term_months))

    elif choice == 10:
        account_number = int(input("Enter your account number: "))
        print(bank.deposit_loan_amount(account_number))
   
    elif choice == 11:
        print("\nList of Accounts:")
        bank.list_accounts()
   
    elif choice == 12:
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")
