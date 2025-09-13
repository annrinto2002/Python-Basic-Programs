num=5
for i in range(3):
    guess=int(input("Guess the number:"))
    if guess==num:
        print("Congratulations")
        break
    else:
        print("Guess is Wrong")
if (i==2 and guess!=num):
    print(f"Sorry you failed to guess.The correct answer is {num}")    
    
    