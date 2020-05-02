# create function to return fibonacci value of any given number
def fibonacci_recursive(j):
    if j == 0:
        return 0
    elif j == 1:
        return 1
    else:
        return fibonacci_recursive(j - 1) + fibonacci_recursive( j - 2)
        
# create function to return fibonacci sequence of any given value
def fibonacci_sequence(j):
    for i in range(j + 1):
        print(fibonacci_recursive(i))
