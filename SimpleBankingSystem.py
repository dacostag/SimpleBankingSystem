import random

class Bank:
    main_menu = ("1. Create an account",
                 "2. Log into account",
                 "0. Exit")
    account_menu = ("1. Balance",
                    "2. Log out",
                    "0. Exit")

    def __init__(self):
        self.passwords = {}
        self.ledger = {}
        self.state = "run"

    def print_main_menu(self):
        print(*self.main_menu, sep="\n")

    def print_account_menu(self):
        print(*self.account_menu, sep="\n")

    def main_loop(self):
        while True:
            self.print_main_menu()
            selection = input()
            if selection == "0":
                self.state = "exit"
            elif selection == "1":
                self.create_account()
            elif selection == "2":
                self.account_loop(self.request_valid_account())  
            else:
                print("\nInvalid selection.\n")          

            if self.state == "exit":
                break

    def create_account(self):
        while True:
            account_num = "400000" + self.random_digits(9)
            account_num += self.luhn_check_num(account_num)
            pin = self.random_digits(4)
            if account_num in self.ledger:
                continue
            break
        self.passwords[account_num] = pin
        self.ledger[account_num] = 0
        print("\nYour card has been created", "Your card number:", account_num, "Your card PIN:", pin + "\n", sep="\n")
    
    def account_loop(self, account_num):
        if not account_num:
            return
        while True:
            self.print_account_menu()
            selection = input()
            if selection == "0":
                self.state = "exit"
            elif selection == "1":
                self.show_balance(account_num)
            elif selection == "2":
                print("\nYou have succesfully logged out!\n")
                break
            else:
                print("\nInvalid selection.\n")

            if self.state == "exit":
                break

    def request_valid_account(self):
        print("\nEnter your card number:")
        account_num = input()
        print("Enter your PIN:")
        pin = input()
        if account_num in self.passwords and self.passwords[account_num] == pin:
            print("\nYou have successfully logged in!\n")
            return account_num
        print("\nWrong card number or PIN.\n")
        return None
    
    def show_balance(self, account_num):
        print("/nBalance:", self.ledger[account_num] + "\n")
    
    @staticmethod
    def random_digits(n):
        """Return n random digits between 0 and 9 as a string."""
        return "".join(str(random.randrange(10)) for _ in range(n))

    @staticmethod
    def luhn_control(digits):
        """Return the Luhn control number as an integer. digits must be an iterable representing the digits to be checked, not including the check."""
        digit_list = [int(n) if i % 2 else int(n) * 2 for i, n in enumerate(digits[::-1])]
        return sum(n - 9 if n > 9 else n for n in digit_list)

    @staticmethod
    def luhn_valid(digits):
        """Return True if the digits comply with the Luhn algorithm, False otherwise."""
        return not (Bank.luhn_control(digits[:-1]) + int(digits[-1])) % 10

    @staticmethod
    def luhn_check_num(digits):
        """Return the Luhn check number for an iterable of digits as a string."""
        return str(Bank.luhn_control(digits) * 9 % 10)


system = Bank()
system.main_loop()