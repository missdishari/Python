# inp=int(input("enter a nuber to reverse - "))
# reverse=0
# while inp!=0:
#     rem=inp%10                 ## reversing a number using while loop
#     reverse=reverse*10+rem
#     inp=int(inp/10)
# print("the reversed number is ",reverse)



num=int(input("enter a nuber to reverse - "))

def reverse_num(reversingval):
    reverse = 0  # this line can be written outside but then it becomes global variable and cant be modified inside the function
    while reversingval>0:

        rem = reversingval % 10                    ## reversing a number using while loop and function
        reverse=reverse*10+rem
        reversingval=int(reversingval/10)


    return  reverse

a=reverse_num(num)
print(a)

