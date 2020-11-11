import time
from datetime import datetime

class ATM:
    def __init__(self, name, pin):
       pass
       #else:
       #     raise ValueError("Invalid Account User")

    def deposit(self):
        print("{'transaction': ['" + datetime.now() "', " + amount +"]}")
        return self.deposit
    
    def withdrawal(self):
        print(datetime.now())
        return self.withdrawal
    
    def check_balance(self):
        print(datetime.now())
        return self.check_balance
    
    def get_transactions(self):
        print(datetime.now())
        return self.get_transactions
    
    def get_withdrawals(self):
        print(datetime.now())
        return self.get_withdrawals

    def get_name(self):
        return self.get_name

    def pin(self):
        return self.pin




name = input("What's your name? ")
print("Accessing", name + "'s Virtual ATM...")
time.sleep(2)
print("Access Authorized")

michael = ATM("Michael", 0815)
michael.deposit(100) 