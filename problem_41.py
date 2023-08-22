num1 = int(input("Enter a number: "))
num2 = int(input("Enter range number: "))

s=0
for i in range(num1, num2+1):
    if(i%2==1):
        s+=i

print("Sum of Odd numbers: ",s)