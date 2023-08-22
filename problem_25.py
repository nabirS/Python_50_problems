def is_anagram(st1, st2):
    st1 = st1.lower()
    st2 = st2.lower()
    cont =0
    for i in st1:
        for j in st2:
            if(i==j):
                cont+=1
    if(len(st1)==cont):
        return True
    else:
        return False
# Main  
st1 = input("Enter first string: ") 
st2 = input("Enter second string: ")
print("The Anagram is: ",is_anagram(st1, st2))
