# Calculate sum of nth number.
num = int(input("Enter a number: "))
s=0
for i in range(0,num+1):
    s+=i
print(f"Sum",s)