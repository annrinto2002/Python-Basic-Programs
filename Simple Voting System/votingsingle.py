Age=int(input("Enter age of the voter:"))
if Age>=18:
    print("Eligible for Voting")
    choice=input("Enter the party you want to vote for:")
    ch=choice.upper()
    if ch == "LDF":
        print("Vote Cast.Thank You!")
    elif ch == "UDF":
        print("Vote Cast.Thank You!")
    elif ch == "BJP":
        print("Vote Cast.Thank You!")
    else:
        print("Invalid Party")
else:
    print("Not Eligible for Voting")



