def basic_operations(a,b):
  '''Perform basic arithmetic operations and Return results in a dictionary'''
  add = a + b
  sub = a - b
  mult = a * b
  div = a / b

  return({'sum':add, 'substract':sub,'product':mult,'quotient':div})

def power_operation(a,b,**kwargs):
  '''Calculate power operation. If 'modulo' is provided in kwargs, calculate modulo'''

  result = a ** b

  if 'modulo' in kwargs:
    value = kwargs['modulo']
    result %= value

  return result

def apply_operations(operation_list):
  