# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        return False
        
        '''
        def same_nodes(node_1, node_2) -> bool:
            if not node_1 and node_2:
                return False
            if node_1 and not node_2:
                return False
            if node_1.val == node_2.val:
                return True
            
            return False
        
        
        queue = collections.deque([p, q])
        
        while queue:
            node_1 = queue.popleft()
            node_2 = queue.popleft()
            if not node_1 and not node_2:
                continue
            if not same_nodes(node_1, node_2):
                return False
            queue.extend([node_1.left, node_2.left, node_1.right, node_2.right])
            
        return True
        '''

'''
EASY

Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:

Input: root = [2,1,3]
Output: [2,3,1]

Example 3:

Input: root = []
Output: []

 

Constraints:

    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100
'''            