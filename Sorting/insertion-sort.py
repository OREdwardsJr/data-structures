nums = [1, 50, 0, -3, 200, 3, 4, 5, 5, 4]


def selection_sort(arr):
    for i in range(1, len(arr)):
        select_sort(i, arr)


def select_sort(idx, arr):
    for i in range(idx - 1, -1, -1):
        j = i
        while j >= 0 and arr[idx] < arr[j]:
            arr[idx], arr[j] = arr[j], arr[idx]
            idx -= 1
            j -= 1


selection_sort(nums)

print(nums)


'''
Analysis of Insertion Sort

Sort Property


Time Complexity
The worst case is when the entire array is sorted in descending order. 
In that case, we have to check N elements and swap N elements for each selected element. 
Hence the time complexity is O(N^2)

Space Complexity	
Since the array is sorted in place and no extra space is used, the space complexity is O(1)

Adaptable
If the array is partially sorted, we'll terminate the sorting loop early. 
In other words, nearly sorted arrays complete very quickly. Hence insertion sort is adaptive

Stable
Insertion sort is a stable sorting algorithm. As elements bubble to the correct position in the sorted area of 
the array, the original relative order of equal elements are maintained.

Number of Comparisons and Swaps
Insertion Sort makes O(N^2) comparisons ( every element is compared to every other element). 
Insertion Sort makes O(N^2) swaps to get all elements in the correct place


When to use and when to avoid Insertion Sort ?

Use insertion sort in the following scenarios:
    When the array is nearly sorted - since insertion sort is adaptive
    When we have memory usage constraints
    When a simple sorting implementation is desired
    When the array to be sorted is relatively small
    When you need to sort elements online - that is sorting them as they come in.

Avoid using insertion sort when:
    The array to be sorted has a large number of elements
    The array is completely  unsorted
    You want a faster run time and memory is not a concern.
'''