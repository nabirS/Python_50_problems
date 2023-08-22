strng = input("Enter a string: ")
count=0
#lst =([*strng])
for i in range(len(strng)):
    if(strng[i]=='a'or
       strng[i]=='e'or
       strng[i]=='i'or
       strng[i]=='o'or
       strng[i]=='u'or
       strng[i]=='A'or
       strng[i]=='E'or
       strng[i]=='I'or
       strng[i]=='O'or
       strng[i]=='U'):
        count+=1

print(count)