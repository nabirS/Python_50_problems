string = input("enter a string: ")
combine_str =string.replace(' ', '')
slicing = combine_str[ :: -1]
if (combine_str == slicing):
    print("Palindrome string")
else:
    print("Not palindrome string")