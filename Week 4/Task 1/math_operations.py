def basic_operations(a,b):
  '''Perform basic arithmetic operations'''
  add = a + b
  sub = a - b
  mult = a * b
  div = a / b

  return({'sum':add, 'substract':sub,'product':mult,'quotient':div})

def power_operation(a,b,**kwargs):

