class ATM:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        self.transaction_history.append(f'Withdrew: ${amount}')
        return f'Withdrew: ${amount}'

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f'Deposited: ${amount}')
        return f'Deposited: ${amount}'

    def change_pin(self, new_pin):
        self.pin = new_pin
        return "PIN changed successfully."

    def view_transaction_history(self):
        return self.transaction_history

# Example initialization
atm = ATM(pin='1234')

# Example usage
print(atm.check_balance())  # Check initial balance
print(atm.deposit(100))    # Deposit money
print(atm.withdraw(30))     # Withdraw money
print(atm.change_pin('4321'))  # Change PIN
print(atm.view_transaction_history())  # View transaction history