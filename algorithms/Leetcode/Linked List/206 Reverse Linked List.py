# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        node = head
        nodes = []
        while node:
            nodes.append(node.val)
            node = node.next
        head = ListNode(nodes.pop(-1))
        node = head
        for elem in nodes[::-1]:
            node.next = ListNode(elem)
            node = node.next
        
        return head