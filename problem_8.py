lst=[]
n = int(input("Enter the size of list: "))
for i in range(0,n):
    item = int(input())
    lst.append(item)
print("Before sorted: ",lst)
for i in range(len(lst)):
    for j in range(1+i, len(lst)):
        if(lst[i]<lst[j]):
            lst[i], lst[j] = lst[j], lst[i]
print("After sorted in dscending order: ",lst)
print("Largest second value: ",lst[1])
