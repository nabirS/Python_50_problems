#find maximum and minimum value.
lst=[]
num= int(input("Enter some numbers: "))

for i in range(0,num):
    ele = int(input())
    lst.append(ele)

max_val=max(lst)
min_val=min(lst)

print(f"Maximum Value",max_val,"\n""Minimum Value",min_val )