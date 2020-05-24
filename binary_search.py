def binary_search(array, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high)//2
        if target == array[mid]:
            return True
        elif target < array[mid]:
            return binary_search(array, target, low, mid - 1)
        else:
            return binary_search(array, target, mid + 1, high)