class Solution:
    def findMin(self, nums: List[int]) -> int:
        count = 0
        lowestNum = nums[0]
        for num in nums[1:]:
            if num < lowestNum:
                return num
            lowestNum = min(num, lowestNum)
        return lowestNum