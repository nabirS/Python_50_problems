lst1 =[]
lst2=[]
n = int(input("enter values range: "))
for i in range(0,n):
    item1 = int(input())
    lst1.append(item1)
    item2=int(input())
    lst2.append(item2)
print("List1: ",lst1)
print("List2: ",lst2)
if (lst1==lst2):
    print("Identical list")
else:
    print("Different list")