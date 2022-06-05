# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        '''
        if not root:
            return True
            
        l = root.left
        r = root.right
        
        if l and  not r or not l and r:
            return False
            
        We can perform a recursive call on each node and compare them to each other
        If we direct l and r in opposing directions then we can easily check for symmetry
        '''
        
        if not root:
            return True
        
        l = root.left
        r = root.right
        
        queue = collections.deque([l, r])
        
        while queue:
            l = queue.popleft()
            r = queue.popleft()
            
            if not l and not r:
                continue
                
            if not l or not r:
                return False
            
            if l.val != r.val:
                return False
            
            queue.extend([l.left, r.right, l.right, r.left])
            
        return True
        
'''
EASY

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:

Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:

Input: root = [1,2,2,null,3,null,3]
Output: false

 

Constraints:

    The number of nodes in the tree is in the range [1, 1000].
    -100 <= Node.val <= 100
'''        