from insertion_sort import insertion_sort
from create_array import create_array
from binary_search import binary_search
from reverse_list import reverse_list

'''
numbers = create_array()
print("Pre-sort: " + str(numbers))
insertion_sort(numbers)
print("Post-sort: " + str(numbers))
'''

nums = list(range(1,20))
reverse_list(nums, 0 , len(nums)-1)
print(nums)
#print(binary_search(nums, 100 , 0, len(nums)-1))