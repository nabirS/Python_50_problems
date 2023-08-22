lst=[]
n = int(input("enter size of list: "))
#For even list
if(n%2==0):
    #Create a list with integers values.
    for i in range(0,n):
      item = int(input())
      lst.append(item)
    length=len(lst)
    lst.sort()
    mid_1 = int(length/2) 
    mid_2 = int(length/2 +1)
    median = int((lst[mid_1-1]+lst[mid_2-1])/2)
    print("Median value: ",median)
# For Odd lists>
else:
    #Create a list with integers values.
    for i in range(0,n):
      item = int(input())
      lst.append(item)
    length=len(lst)
    lst.sort()
    # length=len(lst)
    mid_1 = int((length+1)/2) 
    median =lst[mid_1-1]
    print("Median value: ",median)



   