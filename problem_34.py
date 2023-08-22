lst=[]
lst1 =[]
n = int(input("enter size of list: "))

for i in range(0,n):
    item =input()
    lst.append(item)
for i in lst:
    w_len = len(i)
    lst1.append(w_len)

print(lst1)