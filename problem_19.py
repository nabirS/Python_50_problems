num = int(input("Enter a number: "))
s=0
while(num>0):
    res = num%10
    s=s+res
    num = int(num/10)

print("Sum of digit's number: ",s)