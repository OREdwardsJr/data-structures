'''
    The dynamic solution is much faster, giving us a Time Complexity of
    O(n) while the recursive function gives us a time complexity(2^n + m).
    The high number of recursive calls add to the time complexity,
    given that you are taking two to the power of: n + m, which accounts for 
    fib(n-1) + fib(n-2). The space complexity of the recursive function
    will also be much larger due to the amount of recursive calls in the
    stack.
'''  

class Solution:
    def fib(self, n: int) -> int:
        #Dynamic Programming
        a, b = 0, 1
        
        for i in range(n):
            a, b = a, a + b
            
        return b
        
        
        #Recursive
        '''
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        return Solution().fib(n-1) + Solution().fib(n-2)
        '''
        
'''
EASY
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).

 

Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

 

Constraints:

    0 <= n <= 30

'''