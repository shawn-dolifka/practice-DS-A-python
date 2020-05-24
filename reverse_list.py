def reverse_list(array, start, stop):
    if start < stop:
        temp = array[start]
        array[start] = array[stop]
        array[stop] = temp
        reverse_list(array, start+1, stop-1)
