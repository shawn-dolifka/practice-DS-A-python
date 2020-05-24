import math

def merge(array, low, mid, high):
    #Calculate length of sub-array A[low-mid]
    n1 = mid - low + 1
    #Calculate the length of sub-array A[mid-high]
    n2 = high - mid

    ''' Create a new array for the low-mid values (Left). 
    1 is added to the end for the sentinel (infinity) '''
    left = [0] * n1 + 1
    ''' Create a new array for the mid-high values (Right)
    1 is added to the end for the sentinel (infinity) '''
    right = [0] * n2 + 1

    #Copy the values in the inital array from low-mid
    for i in range(0,n1):
        left[i] = array[low + i -1]
    #Copy the values in the initial array from mid-high
    for j in range(0,n2):
        right[i] = array[mid + j]

    #Add the sentinel in at the end of the left subarray
    left[n1 + 1] = math.inf
    #Add the sentinal in at the end of the right subarray
    right[n2 + 1] = math.inf

    #Initialize index for left subarray
    left_index = 0
    #Initialize index for right subarray
    right_index = 0

    for k in range(low,high):
        if left[left_index] <= right[right_index]:
            array[k] = left[left_index]
            left_index += 1
        else:
            array[k] = right[right_index]
            right_index += 1