lst1=[]
n = int(input("enter string range: "))

for i in range(0,n):
    item1 =(input())
    lst1.append(item1)
lst2=set(lst1)
print(f'After removed of string:{list(lst2)}')