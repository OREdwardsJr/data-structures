class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def explore(grid, r, c) -> int:
            if (r < 0 or r >= len(grid)) or (c < 0 or c >= len(grid[0])):
                return 0
            
            if grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            
            island_count = 1
            island_count += explore(grid, r + 1, c)
            island_count += explore(grid, r - 1, c)
            island_count += explore(grid, r, c + 1)
            island_count += explore(grid, r, c - 1)
            
            return island_count
        
        
        max_island = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                island_len = explore(grid, r, c)
                max_island = max(max_island, island_len)
                    
        return max_island


'''
MEDIUM 

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 50
    grid[i][j] is either 0 or 1.

'''        