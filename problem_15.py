lst1=[]
n = int(input("enter values range: "))

for i in range(0,n):
    item1 = int(input())
    lst1.append(item1)
count_digit= int(input("Enter a count digit: "))
cont=0
for i in lst1:
    if(i==count_digit):
        cont+=1
print(f'Number of {count_digit} exist in the list: {cont} times')