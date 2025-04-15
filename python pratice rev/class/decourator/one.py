class Account:
    def open_acc(self):
        print("Created succesfully")
    def deposit_amount(self,amount):
        print("Amount deposited")
    @classmethod
    def withdraw_amount(cls,amount):
        print("amount withdrawn")
    @staticmethod
    def update_bal():
        print("utility method")
a1=Account()
a1.open_acc()
a1.deposit_amount(500)
a1.withdraw_amount(200)
a1.update_bal()
a2=Account()
a2.open_acc()
a2.deposit_amount(500)
a2.withdraw_amount(100)
a2.update_bal()

