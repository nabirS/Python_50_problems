lst =[]
n = int(input("enter values range: "))
s=0
for i in range(0,n):
    item = int(input())
    lst.append(item)
for i in range(0,n):
    s+=lst[i]
avg =int(s/n)
print("Average: ",avg)

