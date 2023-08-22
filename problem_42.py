import re
e_mail = input("Enter a email name: ")
pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
if (re.match(pat, e_mail)):
    print("Valid email")

else:
    print("Invalid email")