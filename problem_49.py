string = input("Enter a string: ")
upper = 0
lower = 0
for i in  range(len(string)):
    if (ord(string[i]) >= 65 and ord(string[i]) <=90):
      upper+=1

    elif(ord(string[i]) >= 97 and ord(string[i]) <=122):
       lower+=1
print("Uppercase letters: ",upper)
print("Lowercase letters: ",lower)