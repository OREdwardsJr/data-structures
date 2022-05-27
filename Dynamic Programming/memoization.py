"""
MEMOIZATION IS A WAY TO STORE VALUES WITHIN A HASHMAP SO THAT YOU CAN ACCESS A VALUE WITHOUT REPEATING CALLS

Memoization Recipe
1. Make it work
    • Visualize the problem as a tree
    • Implement the tree using recursion (A tree is already a recursive structure)
    • Test it
2. Make it efficient
    • Add a memo object
    • Add a base case to return memo values (EG if key is in memo then return memo[key])
    • Store return values into the memo
"""

"""
# Number of nodes == 2N - Time complexity is O(n) and Space is O(n)
def fib(n, memo={}):
    if n <= 2:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = fib(n - 1) + fib(n - 2)

    return memo[n]


print(fib(100))
"""


"""
GRID TRAVELER

Say that you are a traverler on a 2d grid. You begin in the top-left corner and your goal is to travel
to the bottom-right corner. You may only move down or right.

In how many ways can you travel to the goal on a grid with dimensions m * n
"""


#Brute Force solution
#Time complexity O(2^ (n + m))
#Space O(n + m)
def grid_traveler(m, n):
    if m == 1 & n == 1:
        return 1

    if m == 0 or n == 0:
        return 0

    return grid_traveler(m - 1, n) + grid_traveler(m, n - 1)



#Memoization - Much faster
#O(m * n) time complexity and O(m + n) space
def grid_traveler(m, n, memo={}):
    key = (m, n)

    if key in memo:
        return memo[key]

    if m == 1 & n == 1:
        return 1

    if m == 0 or n == 0:
        return 0

    memo[key] = grid_traveler(m - 1, n) + grid_traveler(m, n - 1)

    return memo[key]

print(grid_traveler(1, 1))
print(grid_traveler(2, 3))
print(grid_traveler(3, 2))
print(grid_traveler(3, 3))
print(grid_traveler(18, 18))
