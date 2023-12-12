def basic_operations(a,b):
  '''Perform basic arithmetic operations and Return results in a dictionary'''
  try:
    add = a + b
    sub = a - b
    mult = a * b
    div = a / b
    result = {'sum':add, 'substract':sub,'product':mult,'quotient':div}
  except ZeroDivisionError:
    return "Can't divide with zero"
  except TypeError:
    return "Invalid input"
  else:
    return result


def power_operation(a,b,**kwargs):
  '''Calculate power operation. If 'modulo' is provided in kwargs, calculate modulo'''
  try:
    result = a ** b

    if 'modulo' in kwargs:
      value = kwargs['modulo']
      result %= value
  except ZeroDivisionError:
    return "Can't divide with zero"
  except TypeError:
    return "Invalid input"
  else:
    return result

def apply_operations(operation_list):