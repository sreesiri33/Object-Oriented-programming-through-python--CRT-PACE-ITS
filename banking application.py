class hdfc:
    def __init__(self):
        self.balance=0
        print("welcome to hdfc")

    def deposit(self):
        amount=float(input("Enter deposit amount:"))
        self.balance+=amount
        print("\n Amount deposited:",amount)
    def withdraw(self):
        amount=float(input("Enter amount to be withdrawn:"))
        if self.balance>=amount:
              self.balance-=amount
              print("\nYou withdrew:",amount)
        else:
              print("\n Insufficient balance")
    def display(self):
        print("\nNet Available Balance=",self.balance)
#driver code
s=hdfc()
s.deposit()
s.withdraw()
s.display()

    
            
        
