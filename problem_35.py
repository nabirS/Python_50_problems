lst=[]
n = int(input("enter size of list: "))

for i in range(0,n):
    item =input()
    lst.append(item)
for i in range(0, len(lst)):
    for j in range(i+1, len(lst)):
        if (lst[i]>lst[j]):
            lst[i], lst[j] = lst[j], lst[i]

print("Sorted in ascending: ",lst)