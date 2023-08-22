lst=[]
n = int(input("enter size of list: "))
cont=0

for i in range(0,n):
    item =input()
    lst.append(item)

fre_ele = max(set(lst), key=lst.count)
print("Most frequent element: ",fre_ele)