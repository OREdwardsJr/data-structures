class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def build_tree(arr):
            head = ListNode(val=arr.pop(0))
            node = head
            for elem in arr:
                node.next = ListNode(val=elem)
                node = node.next
            node.next = None
            return head

        sum_list = []

        node = l1
        while node:
            sum_list.append(node.val)
            node = node.next

        node = l2
        count = 0
        while node:
            try:
                sum_list[count] += node.val
            except:
                sum_list.append(node.val)
            node = node.next
            count += 1

        adder = 0
        for i in range(len(sum_list)):
            sum_list[i] += adder
            if sum_list[i] < 10:
                adder = 0
            else:
                adder = 1
                sum_list[i] -= 10
        
        if adder == 1:
            sum_list.append(1)

        return build_tree(sum_list)



#Debug
def print_tree(tree: object) -> str:
    llstr = ""
    while tree:
        llstr += str(tree.val) + "->"
        tree = tree.next

    return llstr


def build_tree(arr: list) -> object:
    head = ListNode(arr.pop(0))
    node = head
    for elem in arr:
        node.next = ListNode(elem)
        node = node.next
    return head


l1 = build_tree([9, 9, 9, 9, 9, 9, 9])
l2 = build_tree([9, 9, 9, 9])

tree = Solution().addTwoNumbers(l1, l2)
print(print_tree(tree))

'''
MEDIUM
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''