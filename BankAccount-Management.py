class BankAccount:
    def __init__(self, acc_holder, acc_no, balance):
        self.acc_holder = acc_holder
        self.acc_no = acc_no
        self.__balance = balance     # privete variable
        
    def check_balance(self):    # using this function, accessing privatre variable
        print(f"Balance: ₹{self.__balance}")
        
    def deposit(self, amount):
        self.amount = amount
        self.__balance += amount
        print(f"Deposited ₹{amount}")
        print(f"New Balance: ₹{self.__balance}")
        
    def withdraw(self, amount):
        self.amount = amount
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print(f"Withdraw ₹{amount}")
            print(f"Remaining Balance: ₹{self.__balance}")
            
    def profile(self):
        print(f"Account Holder Name: {self.acc_holder}")
        print(f"Account Number: {self.acc_no}")
        
        
babul = BankAccount("Babul Parida",8926102760,20000)
babul.profile()
babul.check_balance()
babul.deposit(5000)
babul.withdraw(500)