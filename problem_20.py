lst1=[]
n = int(input("enter string range: "))

for i in range(0,n):
    item1 =(input())
    lst1.append(item1)
product =1
for i in range(1,len(lst1)+1):
    product*=i

print(f'Product of elements: {product}')    