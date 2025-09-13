nLDF=0
nUDF=0
nBJP=0
while(True):
    age=int(input("Enter the age:"))
    if age>=18:
        print("You are Eligible to vote")
        vote=input("Enter which party to be voted:")
        voted=vote.upper()
        
        if voted=="LDF":
            nLDF+=1
           
        elif voted=="UDF":
            nUDF+=1
          
        elif voted=="BJP":
            nBJP+=1
            
    else:

        print("Not eligible to vote")
    choice=input("Do you want to continue voting (Yes/No):")
    ch=choice.upper()
    if(ch=='NO'):
        break

if(nLDF>=nUDF and nLDF>=nBJP):
    print("LDF has won")
elif(nUDF>=nLDF and nUDF>=nBJP):
    print("UDF won")
else:
    print("BJP won")
print(f"The votes secured by : LDF is {nLDF},UDF is {nUDF}, BJP is {nBJP}")



