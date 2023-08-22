string = input("enter a string: ")
rev_str = string[ :: -1]
if string in rev_str:
    print("Palindrome string")
else:
    print("Not palindrome string")