inp1=int(input("enter the lower limit of the range -"))
inp2=int(input("enter the lower limit of the range -"))
while inp1<=inp2:
    i = 2
    flag=0


    while i<inp1:

        if inp1%i==0:
            flag=1
            break
        else:
            flag=0

            i=i+1
            continue
    if inp1==1:
        flag=1
    if flag==0:

        print(inp1)
    inp1=inp1+1
