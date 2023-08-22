import math
n=int(input("Enter a number: "))
m= int(math.sqrt(n))
if (n==1 or n==0):
    print("Not prime")
elif(n==2 or n==3):
     print("Prime")
else:
    for i in range(2,m+1):
        if(n%i==0):
            print("Not prime")
            break
        else:
            print("Prime")
            break

