def quicksort(array):
    """quicksort, based on the pseudocode from the coursebook"""
    def sort(array, first, last):
        if first < last:
            #i set pivot as the value on last index.
            pivot = array[last]
            i = first-1
            for j in range(first, last):
                if array[j] <= pivot:
                    i += 1
                    temp = array[i]
                    array[i] = array[j]
                    array[j] = temp
            temp = array[i+1]
            array[i+1] = pivot
            array[last] = temp
            sort(array, first, i)
            sort(array, i+1, last)
    first = 0
    last = len(array)-1
    sort(array, first, last)
    return array
