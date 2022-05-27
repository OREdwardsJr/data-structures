
#Brute Force O(2 ** (m + n))
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 & n == 1:
            return 1
        
        if m == 0 or n == 0:
            return 0
        
        return Solution().uniquePaths(m-1, n) + Solution().uniquePaths(m, n - 1)
'''

#Memoization O(m * n) time
class Solution:
    def uniquePaths(self, m: int, n: int, memo={}) -> int:
        if m == 1 & n == 1:
            return 1
        
        if m == 0 or n == 0:
            return 0
        
        key = (m, n)
        
        if key in memo:
            return memo[key]
        
        memo[key] = Solution().uniquePaths(m-1, n) + Solution().uniquePaths(m, n - 1)
        
        return memo[key]