lst=[]
n = int(input("enter size of list: "))

for i in range(0,n):
    item =input()
    lst.append(item)

longest_str = max(lst, key=len)
print("Longest string is: ",longest_str)
