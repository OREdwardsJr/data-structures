class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        nums.sort()
        curr, longest = 0, 0
        
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 1:
                curr += 1
            elif nums[i + 1] == nums[i]:
                continue
            else:
                curr = 0
                
            longest = max(curr, longest)
            
        return longest + 1


'''
MEDIUM

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

 

Constraints:

    0 <= nums.length <= 105
    -109 <= nums[i] <= 109
'''        