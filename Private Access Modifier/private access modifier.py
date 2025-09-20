class BankAccount:
    def __init__(self,account_number,balance):
        self.__account_number=account_number
        self.__balance=balance

    def get_balance(self):
        return self.__balance
    
account=BankAccount("12345567889",5000)

#print(account._balance)

print(account.get_balance())

print(account._BankAccount__balance)