strng = input("Enter a string: ")
lst_string =[]
for i in strng:
    # Remove special characters to check alphanumeric .
    if i.isalnum():
        lst_string.append(i)

join_list =''.join(lst_string)
print("Alphanumeric string: ",join_list)
