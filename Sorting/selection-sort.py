import sys


nums = [1, 5, 29, -1, 30, 7, 2, 1]


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
