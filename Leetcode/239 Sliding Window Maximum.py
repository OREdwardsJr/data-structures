class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        for i in range(k-1):
            while q and q[-1] < nums[i]:
                q.pop()
            q.append(nums[i])
            
        res = []
        for i in range(k-1, len(nums)):
            while q and q[-1] < nums[i]:
                q.pop()
            q.append(nums[i])
            
            res.append(q[0])
            
            # Pop old element out of q if needed. 
            if q[0] == nums[i-k+1]: #if q[0] == first number of the sliding window
                q.popleft()
        
        return res


'''
Explanation - https://leetcode.com/problems/sliding-window-maximum/discuss/998795/Python-Monotonic-Queue-Solution-With-Explanation
HARD

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:

Input: nums = [1], k = 1
Output: [1]

 

Constraints:

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
    1 <= k <= nums.length
'''        