inp=int(input("enter the number to check prime or not -"))
i=2
while i<inp:
    if inp%i==0:
        flag=1
        break
    else:
        flag=0

        i=i+1
        continue
if flag==0:
    print(inp,"is a prime number")
else:
    print(inp,"is not a prime number")












