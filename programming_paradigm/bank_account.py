class BankAccount:
    def __init__(self,account_balance=0.0):
        self.account_balance=account_balance
    def deposit(self,amount):
        if amount > 0:
            self._account_balance += amount
            print(f"Deposit successful. Added ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
            
        if amount <= self._account_balance:
            self._account_balance -= amount
            print(f"Withdrawal successful. Deducted ${amount:.2f}")
            return True
        else:
            print("Withdrawal failed: Insufficient funds.")
            return False
    def display_balance(self):
        print(f"Current Balance: ${self._account_balance:.2f}")
