string = input("Enter a string: ")
p=""  #Null string to put a character once.
for char in string:
    if char not in p: # check in p whwther character has or not. 
        p+=char

print(p)