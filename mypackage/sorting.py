def bubble_sort(items):
    '''Return array of items, sorted in ascending order'''
    for i in range(len(items)):
        for j in range(len(items) -1-i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
    return items

def linear_merge(a, b):
    '''Linear merge fuction'''
    new_list = []
    while len(a) > 0 and len(b) > 0:
        new_list.append((a if a[-1] > b[-1] else b).pop(-1))
    return (new_list + a[::-1] + b[::-1])[::-1]

def merge_sort(items):
    '''Return array of items, sorted in ascending order'''
    if len(items) == 1:
        return items
    mid = int(len(items)/2)
    x = merge_sort(itmes[:mid])
    y = merge_sort(itmes[mid:])
    return linear_merge(x,y)

def quick_sort(items):
    '''Return array of items, sorted in ascending order'''
    if len(items)<=1:
        return items
    pivot = items[index]
    small = []
    large = []
    dup = []

    for i in items:
        if i<pivot:
            small.append(i)
        elif i > pivot:
            large.append(i)
        elif i == pivot:
            dup.append(i)
    small = quick_sort(small)
    large = quick_sort(large)

    return small + dup + large
