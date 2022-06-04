'''
Return the right side view of a binary tree (all values)

Strategy:
    Perform a level-order traversal
        - The last item of our queue will be the node that is apparent
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return root

        self.res.append(root.val)
        
        self.traverse(root)

        return self.res

    def traverse(self, node) -> None:
        q = []

        q.extend([node.left, node.right])

        while q:
            temp = q[:]
            q.clear()
            if temp:
                stack = [node for node in temp if node]
                if stack:
                    self.res.append(stack[-1].val)
            for node in temp:
                if node:
                    q.extend([node.left, node.right])


'''
MEDIUM

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:

Input: root = [1,null,3]
Output: [1,3]

Example 3:

Input: root = []
Output: []

 

Constraints:

    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100
'''                    