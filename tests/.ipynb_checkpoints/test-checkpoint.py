from mypackage import top_n, recursion, sorting

def test_top_n():
    """
    make sure top_n works correctly
    """

    assert top_n.top_n([8, 3, 2, 7, 4], 3) == [8, 7, 4], 'incorrect'
    assert top_n.top_n([10, 1, 12, 9, 2], 2) == [12, 10], 'incorrect'
    assert top_n.top_n([1, 2, 3, 4, 5], 5) == [5, 4, 3, 2, 1], 'incorrect'

def test_sum_array(array):
    '''Test Sum Array: Does the function return a sum of an array'''
    assert recursion.sum_array([8, 3, 2, 7, 4]) == 24
    assert recursion.sum_array([10, 1, 12, 9, 2]) == 34
    assert recursion.sum_array([1, 2, 3, 4, 5]) == 15

def test_fibonacci(n):
    '''Test fibonacci to return nth number in sequence'''

    assert recursion.fibonacci(6) == 8
    assert recursion.fibonacci(12) == 144
    assert recursion.fibonacci(20) == 6765

def test_factorial(n):
    '''Test Factorial: !n'''
    assert recursion.factorial(2) == 2
    assert recursion.factorial(5) == 120
    assert recursion.factorial(7) == 5040

def test_reverse_word(word):
    '''Test to see if the function does reverse the word'''
    assert recursion.reverse('cow') == 'woc'
    assert recursion.reverse('apple') == 'elppa'
    assert recursion.reverse('horseshoe') == 'eohsesroh'

def test_bubble_sort(n):
    '''Test to see if bubble sort sorts correctly'''
    assert sorting.bubble_sort([1,8,79,5,8,9]) == [1, 5, 8, 8, 9, 79]
    assert sorting.bubble_sort([5,8,9,7,4,5]) == [4, 5, 5, 7, 8, 9]

def test_merge_sort(n):
    '''Test to see if merge sort, sorts correctly'''
    assert sorting.merge_sort([1,8,79,5,8,9]) == [1, 5, 8, 8, 9, 79]
    assert sorting.merge_sort([5,8,9,7,4,5]) == [4, 5, 5, 7, 8, 9]

def test_quick_sort(n):
    '''Test to see if quick sort, sorts correctly'''
    assert sorting.quick_sort([1,8,79,5,8,9]) == [1, 5, 8, 8, 9, 79]
    assert sorting.quick_sort([5,8,9,7,4,5]) == [4, 5, 5, 7, 8, 9]
