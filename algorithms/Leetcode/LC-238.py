from re import I


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        i = 0
        for k in range(len(nums)):
            if nums[k] != 0:
                nums[i] = nums[k]
                i += 1

        for j in range(i, len(nums)):
            nums[j] = 0

        return nums

print(Solution().moveZeroes([0,1,0,3,12]) == [1,3,12,0,0])