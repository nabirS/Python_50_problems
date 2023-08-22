#Given number is palindrom or not.
num =int(input("Enter a number: "))
s=0
temp=num
while(num>0):
    r=num%10
    s=(s*10)+r
    num=int(num/10)
if(temp==s):
    print("Palindrome Number")
else:
    print("Not Palindrome number")