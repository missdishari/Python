# variables required are - principal value,rate,time,frequency of compounding
prin=int(input("enter the principal value-"))
rate=int(input("enter the rate - "))
freq=int(input("enter the frequency -"))
time_period =int(input("enter the time in years -"))
CI=prin*((1+(rate/(freq*100)))**(freq*time_period))
print("compound intrest-",CI)

# much more can be added