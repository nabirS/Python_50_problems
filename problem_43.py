import re
string = input("Enter a sentence: ")
#search_key = input("Enter a search key: ")
# Serah by a to find word starts with a.
pattern = r'a\w+'
matches = re.findall(pattern, string)
print(matches)