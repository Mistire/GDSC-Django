# Create a Python module (math_operations.py) with the following functionalities:

## Basic Operations Function:

Create a function basic_operations that takes two numbers and performs basic arithmetic operations (addition, subtraction, multiplication, division). This function should return a dictionary with the results for each operation.

```def basic_operations(a, b):
    # Perform basic arithmetic operations
    # Return results in a dictionary```

## Power Operation Function:
Create a function power_operation that takes a base and an exponent and calculates the result of the power operation. Use the **kwargs feature to allow the user to specify an optional modulo value. If the modulo value is provided, calculate the result modulo the specified value.

```def power_operation(base, exponent, **kwargs):
    # Calculate power operation
    # If 'modulo' is provided in kwargs, calculate modulo```


## Exception Handling:
Add appropriate exception handling in both functions to handle cases such as division by zero and invalid inputs.
In the same module, create a higher-order function apply_operations that takes a list of tuples, where each tuple contains a function and its corresponding arguments. Use map to apply each function to its arguments and return a list of results.

```def apply_operations(operation_list):
    # Use map to apply each function to its arguments
    # Return a list of results```


Create a script (main.py) to test your module:
from math_operations import basic_operations, power_operation, apply_operations

### Test basic_operations

```result_basic = basic_operations(10, 5)
print("Basic Operations Result:", result_basic)```

### Test power_operation

```result_power = power_operation(2, 3)
print("Power Operation Result:", result_power)```

### Test power_operation with modulo

```result_power_modulo = power_operation(2, 3, modulo=5)
print("Power Operation with Modulo Result:", result_power_modulo)```

# Test apply_operations

```operations = [
    (lambda x, y: x + y, (3, 4)),
    (lambda x, y: x * y, (2, 5)),
]
```