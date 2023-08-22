strng = input("Enter a string: ")
word_split = strng.split()
longest_word = max(word_split, key=len)
print(f"longest word length: ",len(longest_word))