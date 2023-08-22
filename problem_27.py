#average even numbers between two numbers.
num1 = int(input("enter a number to start: "))
num2 = int(input("enter a number to end: "))
cont =0
s=0
for i in range(num1, num2+1):
    if(i%2==0):
        cont+=1
        s+=i
avg = s/cont
print("Average is: ",avg)