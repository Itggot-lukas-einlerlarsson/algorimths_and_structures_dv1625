def insertionsort(lst):
    """insertionsort, based on the pseudocode from the coursebook"""
    for index in range(1, len(lst)): 
        key = lst[index]
        sort_i = index-1
        while sort_i >= 0 and lst[sort_i] > key:
            lst[sort_i+1] = lst[sort_i]
            sort_i -= 1
        lst[sort_i+1] = key
    return lst
