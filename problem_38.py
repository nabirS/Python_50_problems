lst_tup = []
n = int(input("enter size of list: "))

for i in range(0,n):
    item =tuple(input())
    lst_tup.append(item)

remove_tuple = set(lst_tup)
turn_list = list(remove_tuple)
print(turn_list)
