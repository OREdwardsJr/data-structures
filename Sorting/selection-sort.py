import sys

nums = [1, 5, 29, -1, 30, 7, 2, 1]
# nums = [0, 0, 0]
# nums = []
# nums = [1]


def selection_sort(nums):
    for i in range(len(nums)):
        j = smallest_idx(i, nums)
        nums[i], nums[j] = nums[j], nums[i]

    return


def smallest_idx(idx, arr):
    min_val = sys.maxsize
    min_idx = 0

    for i in range(idx, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
            min_idx = i

    return min_idx


selection_sort(nums)
print(nums)



'''
When to use and when to avoid Selection Sort?

Use selection sort in the following scenarios:

    When the array is NOT partially sorted
    When we have memory usage constraints
    When a simple sorting implementation is desired
    When the array to be sorted is relatively small

Avoid using Selection sort when:

    The array to be sorted has a large number of elements
    The array is nearly sorted
    You want a faster run time and memory is not a concern.


Analysis of Selection Sort

Time Complexity
    For each element, the entire list is checked to find the smallest element. 
So in the worst case, "n" elements are checked for each element. Hence the time complexity is O(N^2)

Space Complexity
Since the array is sorted in place and no extra space is used, the space complexity is O(1)

Adaptable
    The order of elements does not affect the sorting time. 
In other words, even if the array is partially sorted, still each element is compared and there is no 
breaking out early. Hence Selection sort is non-adaptable.

Stable
    Selection sort is NOT a stable sorting algorithm. 
Elements which are equal might be re-arranged in the final sort order relative to one another.

Number of Comparisons and Swaps
	Selection Sort makes O(N^2) comparisons ( every element is compared to every other element). 
    Selection Sort makes O(N) swaps to get all elements in the correct place.    
'''