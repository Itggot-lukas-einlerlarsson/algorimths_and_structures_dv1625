def heapsort(array):
    """heapsort, based on the pseudocode from the coursebook"""
    def max_heapify(array, n, i):
        parent = i # put root as parent(largest value in subarray) first
        left = i*2
        right = i*2+1

        #if left in heap-size and has bigger value than parent
        if left < n and array[left] > array[parent]:
            parent = left

        #if right in heap-size and has bigger value than parent
        if right < n and array[right] > array[parent]:
            parent = right

        #if parent isnt the intial root index:
        if parent != i:
            temp = array[i]
            array[i] = array[parent]
            array[parent] = temp
            max_heapify(array, n, parent) # doing it recursively to assure max-heap

    n = len(array) #heap-size

    for i in range(int(n/2)-1, -1, -1):
        #print(i)
        max_heapify(array, n, i)

    #print("max_heapified: ", array)

    for i in range(n-1, 0, -1): #n-1 = whole binarytree
        temp = array[0]
        array[0] = array[i]
        array[i] = temp
        max_heapify(array, i, 0)

    #print("sorted: ", array)

    return array
