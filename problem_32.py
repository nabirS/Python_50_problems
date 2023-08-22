lst=[]
n = int(input("enter size of list: "))
# Create a list of integers.
for i in range(0,n):
    item = int(input())
    lst.append(item)
print("Lists: ",lst)
#ascending the list.
for i in range(0, len(lst)):
    for j in range(i+1, len(lst)):
        if(lst[i]>lst[j]):
            lst[i], lst[j] = lst[j], lst[i]

print("After ascending List: ",lst)
print("Second smallest number: ",lst[1])