def bubble_sort(items):
    '''Return array of items, sorted in ascending order'''
    for i in range(len(items)):
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
    return items

def linear_merge(a, b):
    '''Linear merge fuction'''
    new_list = []
    while len(a) > 0 and len(b) > 0:
        new_list.append((a if a[-1] > b[-1] else b).pop(-1))
    return (new_list + a[::-1] +b[::-1])[::-1]

def merge_sort(items):
    '''Return array of items, sorted in ascending order'''
    if len(items) == 1:
        return items
    midpoint = int(len(items)/2)
    x = merge_sort(items[:midpoint])
    y = merge_sort(items[midpoint:])
    return linear_merge(x,y)

def quick_sort(items, index = 0):
    '''Return array of items, sorted in ascending order'''
    if len(items)<=1:
        return items
    i_i = items[index]
    small = []
    large = []
    duplicate = []

    for i in items:
        if i < i_i:
            small.append(i)
        elif i > i_i:
            large.append(i)
        elif i == i_i:
            duplicate.append(i)
    small = quick_sort(small)
    large = quick_sort(large)

    return small + duplicate + large
