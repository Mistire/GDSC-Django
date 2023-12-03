vowels = ["a", "i", "e", "o", "u"]

letter = input("Enter a character to be printed: ")
if letter in vowels:
  print("Vowels are not allowed in the input")
elif len(letter) > 1:
  print("The length of the character should be 1")
else:
  for i in range(1, 6):
      print(((2 * i) - 1) * letter)