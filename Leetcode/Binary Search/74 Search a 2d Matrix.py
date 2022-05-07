class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for row in matrix:
            if row[0] <= target <= row[-1]:
                l = -1
                r = len(row)
                m = (r + l) // 2
                while (r - l) > 1:
                    if row[m] == target:
                        return True
                    elif target > row[m]:
                        l = m
                    else:
                        r = m
                    m = (r + l) // 2
                    print(row[m], l, r)
        return False


#matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
#target = 3
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13


print(Solution().searchMatrix(matrix, target))
