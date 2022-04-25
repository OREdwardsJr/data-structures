class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next == None:
            return head.next
        hash_map = {}
        node = head
        count = 1

        while node:
            hash_map[count] = node
            node = node.next
            count += 1

        hash_map[count] = None

        if count - 1 == n:
            return head.next
            
        if count == 3:
            if n == 1:
                head.next = None
                return head
            else:
                return head.next

        hash_map[count - (n + 1)].next = hash_map[count - (n - 1)]

        return head


def print_tree(head: ListNode) -> list:
    if head == None:
        return head
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


tree = build_tree([1, 2, 3, 4, 5])
# answ = Solution().removeNthFromEnd(tree, 2)
# answ = Solution().removeNthFromEnd(tree, 1) # Remove tail
answ = Solution().removeNthFromEnd(tree, 5)  # Remove head
print(print_tree(answ))
