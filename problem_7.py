#Reverse a given list of integers.
#n_lst=(input("Enter some integers:").split())
# lst =[4,7,9,10,15]
# lst.reverse()
# print(lst)
lst =[]
n = int(input("Enter the size of list: "))
for i in range(0,n):
    item = int(input())
    lst.append(item)
lst.reverse()
print("Reverse items:",lst)