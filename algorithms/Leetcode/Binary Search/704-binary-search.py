class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = -1
        r = len(nums)
        m = (l + r) // 2

        while True:
            if target == nums[m]:
                return m
            elif r - l == 1:
                return -1
            elif target < nums[m]:
                r = m
                m = (l + r) // 2
            elif target > nums[m]:
                l = m
                m = (l + r) // 2