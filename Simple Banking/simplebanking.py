initialamt=int(input("Enter the initial amount:"))
while(True):
    choice=input("Do you want to continue(Yes/No):")
    ch=choice.title()
    if(ch=="Yes"):
        trans=input("Which transaction to be performed:")
        transaction=trans.title()

        if transaction=="Deposit":
            Deposit=int(input("Enter amt to be deposited:"))
            initialamt=Deposit+initialamt
            print(f"Balance={initialamt}")
        elif transaction=="Withdraw":
            Withdraw=int(input("Enter amt to be withdrawn:"))
            if Withdraw<initialamt:
                initialamt=initialamt-Withdraw
                print(f"Balance={initialamt}")
            else:
                print("Insufficient Balance")
    else:
        break
    




