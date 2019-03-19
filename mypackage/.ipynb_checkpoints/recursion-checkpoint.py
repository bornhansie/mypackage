def sum_array(array):
    '''Return sum of all items in array'''
    if len(array) == 0:
        return 0
    else:
        return array[0]+sum_array(array[1:])

def fibonacci(n):
    '''return nth term in fibonacci sequence'''
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

def factorial(n):
    '''return n!'''
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def reverse(word):
    '''return word in reverse'''
    if len(word) == 0:
        return word
    else:
        return reverse(word[1:]) +word[0]