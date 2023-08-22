lst=[]
n = int(input("enter size of list: "))

for i in range(0,n):
    item =input()
    lst.append(item)

lst1=[]
m = int(input("enter size another list: "))

for j in range(0,m):
    item1 =input()
    lst1.append(item1)

A_inters_B = set(lst) & set(lst1)
print(list(A_inters_B))