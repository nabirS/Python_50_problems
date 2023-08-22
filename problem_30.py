num = int(input("Enter a number: "))
power = int(input("Enter a power number: "))
P_number=1
for i in range(1, power+1):
    P_number = P_number*num

print("Power of a number: ",P_number)