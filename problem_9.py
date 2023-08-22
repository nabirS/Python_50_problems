lst =[]
n = int(input("enter values range: "))
for i in range(0,n):
    item = int(input())
    lst.append(item)

print(f"Before removing duplicates the list: ",lst)
conv_set = set(lst)
print(f"After remove duplicates: ",list(conv_set))