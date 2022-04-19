class Solution:
    def isHappy(self, n: int) -> bool:
        #Grab next number
        #If n // 10 < 1 then it's a single digit therefor it is the next number
        def get_next(n: int) -> int:
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum

        # Check if n is already visited
        visited = set()
        while n != 1 and n not in visited:
            visited.add(n)
            n = get_next(n)

        return n == 1

print(Solution().isHappy(19))

"""
EASY 

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:

Input: n = 2
Output: false

 

Constraints:

    1 <= n <= 231 - 1


"""
