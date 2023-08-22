lst=[]
n = int(input("enter size of list: "))
s=0
cont=0
for i in range(0,n):
    item = int(input())
    lst.append(item)

for j in range(1, len(lst)+1):
    if(j%2==0):
        s+=j
        cont+=1
avg =(s/cont)
print("Average of even numbers: {:.2f}".format(avg))
