string = input("Enter a string: ")
vowels = ['a','A', 'e','E', 'i','I', 'o','O', 'u','U']
output = ""
for char in string:
    if (char not in vowels):
        output=output + char

print(output)