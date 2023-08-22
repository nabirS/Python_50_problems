def intersection(lst1, lst2):
    list3 =list(set(lst1) & set(lst2))
    return list3   
lst1 =[]
lst2=[]

n = int(input("enter values range: "))

print("Enter value of first list: ")
for i in range(0,n):
    item1 = int(input())
    lst1.append(item1)
print("Enter value of second list: ")
for j in range(0,n):
    item2 = int(input())
    lst2.append(item2)
    
print(intersection(lst1, lst2))
