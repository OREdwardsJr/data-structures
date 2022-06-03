class Solution():
    def __init__(self):
        self.res = []

    def permute(self, nums: list[int]) -> list[list[int]]:
        self.backtrack(nums)
        return self.res

    def backtrack(self, nums, path=[]):
        if not nums:
            self.res.append(path)
        for x in range(len(nums)):
            self.backtrack(nums[:x] + nums[x+1:], path+[nums[x]])

'''
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        # base case
        if len(nums) == 1:
            return [nums[0]]

        result = []

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)

            result.extend(perms)
            nums.append(n)

        return result'''


print(Solution().permute([1, 2, 3]))

"""
MEDIUM

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]]

 

Constraints:

    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    All the integers of nums are unique
"""
