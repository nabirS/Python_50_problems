lst=[]
n = int(input("enter size of list: "))
cont=0

for i in range(0,n):
    item =input()
    lst.append(item)
for i in range(0, len(lst)):
    for j in range(i+1, len(lst)):
        if (lst[i]==lst[j]):
            cont+=1

if cont==1:
    print("Elements are not unique")
else:
    print("Elements are unique.")