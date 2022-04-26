class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = []
        for i in range(0,numRows):
            if i==0:
                res.append([1])
            elif i==1:
                res.append([1,1])
            else:
                curr = [1] #every row begins with 1
                for j in range(1,len(res[-1])):
                    curr.append(res[-1][j-1]+res[-1][j])
                curr.append(1) #every row ends with 1
                res.append(curr) 
        return res

