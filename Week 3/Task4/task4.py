sum = 0
three_mul = 0
five_mul = 0
for i in range(1, 51):
  if i % 3 == 0:
    print("Three")
    three_mul += 1
  elif i % 5 == 0:
    print("Five")
    five_mul += 1
  else:
    sum += i
    
print(f"The Total Sums of evens are: {sum}")
print(f"Count of numbers replaced with 'Three': {three_mul}")
print(f"Count of numbers replaced with 'Five': {five_mul}")