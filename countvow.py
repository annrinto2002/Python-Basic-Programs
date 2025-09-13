str=input("Enter a string:")
count=0
for i in str:
    if i in 'aeiouAEIOU':
        count=count+1
print(count)
