class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        Recursive method to check surrounding islands
            - Helper method to explore surrounding islands DONE
        
        Need a visited set to prevent infinite recursion and to track which
            islands that have been visited DOONE
        
        Two for loops DONE
            - Check for an island
                - If there's an island then we capture all surrounding island 
                pieces
                else: continue
                
        Control movement around grid utilizing positions (r, c) DONE

        IMPORTANT - It's bad practice to changed a passed in value. So in production, we would use a visited set.
        However, theoretically, this works for coding challenges.
        '''
        count = 0
        
        def explore(grid, r, c) -> bool:
            row_inbounds = r >= 0 and r < len(grid)
            col_inbounds = c >= 0 and c < len(grid[0])
            
            if not row_inbounds or not col_inbounds:
                return False

            if grid[r][c] == "0":
                return False

            grid[r][c] = "0"
            
            explore(grid, r - 1, c)
            explore(grid, r + 1, c)
            explore(grid, r, c - 1)
            explore(grid, r, c + 1)
        
            return True
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):                
                if explore(grid, r, c):
                    count += 1
                        
        return count


'''
MEDIUM

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.

'''