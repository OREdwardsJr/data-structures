class Solution:
    def __init__(self):
        self.res = []
    def combine(self, n: int, k: int) -> List[List[int]]:
        '''
        Given n and k, return all possible combinations of k numbers
        out of range(1, n + 1) 
            • n should be included in your combinations
        Do not return inversed nums
        Use number only once
        
        System
            - Iterate through range
            - Permute i with nums[i+1:]
            - Append to result when len(path) == 2
            - Return result
            
        Methodology
            - Helper method for permutation
            - Initiate result output in constructor
            
        Edge Cases
            - n == 1: return [n]
            - k == n: return [n]
                n = [1,2,3,4], k = 4 => [1,2,3,4]
        '''
        if n == k:
            return [[*range(1, n+ 1)]]
        
        nums = [*range(1, n + 1)]
        self.backtrack(nums, limit = k)
            
        return self.res
    
    def backtrack(self, nums, limit, path=[]):
        if len(path) == limit:
            self.res.append(path)
            return
        
            
        for x in range(len(nums)):
            self.backtrack(nums[x+1:], limit, path=path + [nums[x]])


'''
MEDIUM

77. Combinations
Medium

Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

Example 2:

Input: n = 1, k = 1
Output: [[1]]

 

Constraints:

    1 <= n <= 20
    1 <= k <= n

Accepted
531,867
Submissions
826,866
'''            