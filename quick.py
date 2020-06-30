def quick_sort_in_place(array, start, end):
    if start < end:
        
        if start + 1 == end:
            if array[start] > array[end]:
                larger = array[start]
                array[start] = array[end]
                array[end] = larger
        
        pivot = np.random.randint(start, end+1)
        pivot_value = array[pivot]
        
        array[pivot] = array[-1]
        array[-1] = pivot_value
        
        border = start - 1
        
        for i in range(start, end):
            if array[i] < pivot_value:
                border += 1
                border_value = array[i]
                array[i] = array[border]
                array[border] = border_value
        array[-1] = array[border+1]
        array[border+1] = pivot_value
        
        array = quick_sort_in_place(array, start, border+1)
        array = quick_sort_in_place(array, border+2, end)
    return array
