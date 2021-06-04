# inp=int(input("enter the number you want factorial of -"))
# def factorial(inp):
#     if inp==0:
#         return 1
#     elif inp==1:
#         return 1
#     else:
#
#         mul=inp*factorial(inp-1)
#         return mul
#
# fact=factorial(inp)
# print(fact)


inp=int(input("enter a number to find factorial of -"))
i=inp
fact=1
while i>=1:
    fact=fact*i
    i=i-1
print("the factorial of",inp,"is",fact)
