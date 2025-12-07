
class BankAccount:
    def __init__(self,initial_balance = 0 ):
        self.account_balance = initial_balance

    def deposit(self,amount):
        self.amount = amount 
        # to add deposit to balance
        self.account_balance += amount
        print ( f"Deposited : {amount} , balance {self.account_balance}")

    def withdraw(self,amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"Withdrew: ${amount:,.2f} , balance {self.account_balance}")
            return True
        else:
            print("Transaction failed: Insufficient funds.")
            return False

    def display_balance(self):
        """s
        Prints the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.account_balance:,.2f}")


    
