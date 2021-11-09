class BankAccount:
    bank_name = "PayPy"

    def __init__(self, _balance=0):
        self._balance = _balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def print_balance(self):
        print(f"The current balance is {self._balance}")


def main():
    yael = BankAccount(100000)
    michal = BankAccount(100)
    itay = BankAccount()

    yael.withdraw(300)
    michal.deposit(150)
    itay.deposit(150)

    yael.print_balance()
    michal.print_balance()
    itay.print_balance()

    # yael.bank_name = "Bankont"
    print(f"{BankAccount.bank_name} has a lot of customers. Yael is a customer of {yael.bank_name}.")


if __name__ == '__main__':
    main()
