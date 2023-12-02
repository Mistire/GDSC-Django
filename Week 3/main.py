

list = [i for i in range(1, 10)]
print(list)

#1

for i in range(1, 101):
  if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  else:
    print(i)

#2
isContinue = True
while(isContinue):
  num = int(input("Enter a number: "))
  if num % 2 == 0 and num != 0:
    print("Even Number")
  elif num % 2 != 0:
    print("Odd Number")
  elif num == 0:
    isContinue = False

print("Exited")

#3
words = input("Enter a word: ")
words = [len(i) for i in words.split()]
print(words)

for i in range(90, 64, -1):
  if i % 2 == 0:
     char = chr(i).lower()
  else:
     char = chr(i)
  print(char)

animals = ['lion', 'tiger', 'monkey', 'elephant', 'frog']
filtered_animal = [animal.title() for animal in animals]
print(filtered_animal)