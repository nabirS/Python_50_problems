#Given a list of integers, remove all the even numbers
lst1=[]
n = int(input("enter values range: "))

for i in range(0,n):
    item1 = int(input())
    lst1.append(item1)
for i in lst1:
    if(i%2==0):
        lst1.remove(i)
print(lst1)