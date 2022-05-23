class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 2:
            return min(height[0], height[1]) ** 2
        
        area, max_area = 0, 0
        l = 0
        r = len(height) - 1
        
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
            max_area = max(max_area, area)
            
        return max_area


'''
MEDIUM 

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

EXAMPLE:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.


Constraints:

    n == height.length
    2 <= n <= 105
    0 <= height[i] <= 104

'''        