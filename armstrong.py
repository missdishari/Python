# # this is using function
# num=int(input("enter a number to check armstrong or not  - "))
# copy=num
#
# def pallindrome(num):
#     sum=0
#     while(num):
#         rem = num % 10
#         rem = rem * rem * rem
#         sum = sum + rem
#         num=int(num/10)
#     return sum
#
#
# calculated_val=pallindrome(num)
# if (calculated_val==copy):
#      print("this is an armstrong number")
# else:
#      print("this is NOT an armstrong number")


# this is using loop
num = int(input("enter a number to check armstrong or not  - "))
copy = num

sum = 0
while (num):

    rem = num % 10
    rem = rem * rem * rem
    sum = sum + rem
    num = int(num / 10)

if (sum == copy):
    print("this is an armstrong number")
else:
    print("this is NOT an armstrong number")







