class BankAccount:
    def __init__(self,account_number,balance):
        self.__account_number=account_number #Private attribute
        self.__balance=balance #Private attribute

    def get_balance(self):
        return self.__balance #Accessing private attribute inside the class

#Creating an object
account=BankAccount("12345567889",5000)

#Accessing private attributes directly (Not allowed)
#print(account._balance) #Attribute Error

#Accessing private Attribute using method
print(account.get_balance())

#Accessing private variable using name mangling
print(account._BankAccount__balance) #Allowed but NOT recommended