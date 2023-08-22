import math

def p_square(num):
    sqroot = math.sqrt(num)
    if (sqroot.is_integer()):
        return True
    else:
        return False
    
num = int(input("Enter a number: "))
if (p_square(num)==True):
    print(f'{num} is perfect square.')
else:
    print("Not perfect square")

#print(p_square(num))