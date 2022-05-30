from collections import deque

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return head
        
        q = deque([])
        early_nodes = deque([])
        node_count, count = 0, 0

        node = head
        
        while node:
            node_count += 1
            node = node.next
            
        node = head
        k = k % node_count
        
        while node:
            if count < k:
                early_nodes.append(node)
            q.append(node.val)
            if count >= k:
                node.val = q.popleft()
            node = node.next
            count += 1
            
        
        while q:
            node = early_nodes.popleft()
            node.val = q.popleft()
            
        return head


'''
MEDIUM 

Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:

Input: head = [0,1,2], k = 4
Output: [2,0,1]

 

Constraints:

    The number of nodes in the list is in the range [0, 500].
    -100 <= Node.val <= 100
    0 <= k <= 2 * 109

Accepted
563,838
Submissions
1,610,142
'''        