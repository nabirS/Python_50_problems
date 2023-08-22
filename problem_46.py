import math
n = int(input("Enter first number: "))
n1 = int(input("Enter a range number: "))

for val in range(n, n1):
    if(val>1):
        for i in range(2, val):
            if(val%i==0):
                break
        else:
            print(val, end=' ')
          