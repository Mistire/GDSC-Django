is_palindrome = False
word = input("Enter the word to check: ").lower()

if word == word[::-1]:
  is_palindrome = True
  print(f"The word {word} is a palindrome")
else:
  print(f"The word {word} is not a palindrome,\nbecause {word[::-1]} is not equal to {word} ")