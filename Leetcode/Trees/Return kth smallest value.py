'''
Return the kth smallest number in a BST
If no node return -1

Strategy:
    Perform in-order traversal
    Utilize recursion and pass a counter variable
    Base condition:
    counter == k: return node.val

    TC = O(n)
    SC = O(n)

Edge Cases:
    No root
    Only one subtree
    No children
    Imbalanced BST    
'''

class BST():
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = self.in_order_traversal(root)
        return nodes[k - 1]

    def in_order_traversal(self, root) -> list:
        if not root:
            return 

        elements = []

        elements += self.in_order_traversal(root.left)
        elements.append(root.val)
        elements += self.in_order_traversal(root.right)

        return elements 


'''
MEDIUM

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

Example 1:

Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

 

Constraints:

    The number of nodes in the tree is n.
    1 <= k <= n <= 104
    0 <= Node.val <= 104

 

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
'''        