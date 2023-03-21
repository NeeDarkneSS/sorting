def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(1, n-i):
            if lst[j-1] > lst[j]:
                lst[j-1], lst[j] = lst[j], lst[j-1]
    return lst


