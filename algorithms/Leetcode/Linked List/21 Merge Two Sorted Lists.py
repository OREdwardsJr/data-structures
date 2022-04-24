# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 == None and list2 == None:
            return list1
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1
        else:
            if list2.val < list1.val:
                list3 = ListNode(list2.val)
                node1 = list1
                node2 = list2.next
            else:
                list3 = ListNode(list1.val)
                node1 = list1.next
                node2 = list2
            node3 = list3

            while node1 != None or node2 != None:
                if node1 is None:
                    while node2:
                        node3.next = ListNode(node2.val)
                        node3 = node3.next
                        node2 = node2.next
                elif node2 is None:
                    while node1:
                        node3.next = ListNode(node1.val)
                        node3 = node3.next
                        node1 = node1.next
                else:
                    if node2.val < node1.val:
                        node3.next = ListNode(node2.val)
                        node3 = node3.next
                        node2 = node2.next
                    else:  # node1.val <= node2.val
                        node3.next = ListNode(node1.val)
                        node3 = node3.next
                        node1 = node1.next

        return list3


def print_tree(node: ListNode) -> list:
    elements = []
    while node:
        elements.append(node.val)
        node = node.next
    return elements


def build_tree(arr: list) -> ListNode:
    head = ListNode(arr.pop(0))
    node = head
    for elem in arr:
        node.next = ListNode(elem)
        node = node.next
    return head


llist1 = build_tree([-9, 3])
llist2 = build_tree([5, 7])

new_list = Solution().mergeTwoLists(llist1, llist2)
print(print_tree(new_list))
# list1 = [1,2,4], list2 = [1,3,4]


"""'
EASY

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""
