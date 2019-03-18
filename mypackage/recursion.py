def sum_array(array):
    '''Return sum of all items in array'''
    return sum(array)

def fibonacci(n):
    '''return nth term in fibonacci sequence'''
    if n == 0:
        return 1
    elif n==1 or n==2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

def factorial(n):
    '''return n!'''
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def reverse(word):
    '''return word in reverse'''
    return word[::-1]
