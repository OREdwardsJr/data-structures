class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        #if head == []:
           # return  # something
        count = 1
        node = head

        # Get length of list
        # Get first node
        while node:
            if count == k:
                first_node = node
            node = node.next
            count += 1

        # Get value of count - k
        count_2 = 1
        node = head
        while node:
            if count_2 == count - k:
                second_node = node
                break
            count_2 += 1
            node = node.next

        # Swap Nodes
        temp = first_node.val
        first_node.val = second_node.val
        second_node.val = temp

        return head


def print_tree(head: ListNode) -> list:
    node = head
    llstr = []
    while node:
        llstr.append(node.val)
        node = node.next
    return llstr


def build_tree(arr: list) -> ListNode:
    head = ListNode(arr.pop(0))
    node = head
    for elem in arr:
        node.next = ListNode(elem)
        node = node.next
    return head


#arr = [1, 2, 3, 4, 5] k = 2
#arr = [7,9,6,6,7,8,3,0,9,5] k = 5
arr = [5]
llist = build_tree(arr)

solution = Solution().swapNodes(head=llist, k=1) 
print(print_tree(solution))
