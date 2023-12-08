# Function
#a
def greet(name):
  print(f"Hello {name}")

name = input("Enter your name: ")
greet(name)

#b
def add_numbers(num1, num2):
  return num1 + num2

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

sum = add_numbers(num1, num2)
print(f"The sum of {num1} and {num2} is {sum}")

#Usage of *args
#a
def print_args(*args):
  print(args)

print(1,3,4,56,6)

#b
def calc_average(*args):
  total = sum(args)
  ave = total / len(args)
  print(ave)

calc_average(2,3,5,6,8,7)

# lambda function
# a
lambda_add = lambda x, y: x + y

result = lambda_add(4,6)
print(result)

#b 
lambda_square = lambda x: x**2
result = lambda_square(3)
print(result)

#c
lambda_even = lambda x: x % 2 == 0

result = lambda_even(9)
print(result)

# Filter Function
# a
num = [1,2,3,4,5,6,7,8]
even_num = filter(lambda x: x % 2 == 0, num)
print(list(even_num))

# b
num = [1,2,3,4,5,6,7,8]
double_num = map(lambda x: x*2, num)
print(list(double_num))

#try catch
# a
def sum(num1, num2):
  try:
    int(num1) + int(num2)
  except ValueError:
    print("Incorrect input data type")
  else:
    return num1 + num2

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
print(sum(num1, num2))

#b
def divide(x,y):
  try:
    x/y
  except ZeroDivisionError:
    print("Please don't use 0")
  else:
    return x/y
  
num1 = int(input())
num2 = int(input())
print(divide(num1, num2))