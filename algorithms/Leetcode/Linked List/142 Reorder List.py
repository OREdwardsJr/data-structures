# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []
        node = head
        while node.next:
            node = node.next
            nodes.append(node)

        node = head
        count = 0
        while nodes != []:
            if count % 2 == 0:
                node.next = nodes.pop()
            else:
                node.next = nodes.pop(0)
            node = node.next
            count += 1
        node.next = None


"""
MEDIUM

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.
"""
