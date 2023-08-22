lst=[('nabir', 2), ('akash', 4), ('Masum', 3), ('Mahfuz', 7)]

for i in range(0, len(lst)):
    for j in range(i+1, len(lst)):
        if (lst[i][1]>lst[j][1]):
            lst[i], lst[j] = lst[j], lst[i]

print("Sorted (by second element) in ascending: ",lst)