num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
choice=input("Enter which operation to be performed:")
ch=choice.upper()
if ch=="ADDITION":
    sum=num1+num2
    print(f"Sum={sum}")
elif ch=="SUBTRACTION":
    difference=num1-num2
    print(f"Difference={difference}")
elif ch=="MULTIPLICATION":
    product=num1*num2
    print(f"Product={product}")
elif ch=="DIVISION":
    quotient=num1/num2
    print(f"Quotient={quotient}")
elif ch=="REMAINDER":
    remainder=num1%num2
    print(f"Remainder={remainder}")
else:
    print("Invalid Operator")

          

