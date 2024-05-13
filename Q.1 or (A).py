# Define a decorator function
def check_even_odd(func):
    def wrapper(num1,num2):
        result = func(num1,num2)  # Call the original function
        if result % 2 == 0:
            print(f"The result {result} is even.")
        else:
            print(f"The result {result} is odd.")
        return result
    return wrapper

# Define functions to be decorated
@check_even_odd
def add(a, b):
    return a + b

@check_even_odd
def multiply(a, b):
    return a * b

# Call the decorated functions
result1 = add(2, 5)
result2 = multiply(4, 6)
