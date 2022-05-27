class HeapNode:
    def __init__(self, val) -> None:
        self.data = val
        self.left = None
        self.right = None

    def add_child(self, elem) -> None:
        if not self.left:
            self.left = HeapNode(elem)
        elif not self.right:
            self.right = HeapNode(elem)
        else:
            self.left.add_child(elem)

    def level_order_traversal(self) -> list:
        q = [self]
        elements = list()

        while q:
            temp = q.pop(0)
            elements.append(temp.data)
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)

        return elements


def build_tree(arr: list) -> HeapNode:
    root = HeapNode(arr.pop(0))

    for elem in arr:
        root.add_child(elem)

    return root


nums = [23, 3, 5, 68, 2, 1, -20, 300, 233, 54, 28, 92, 0]
num_tree = build_tree(nums)
print(num_tree.level_order_traversal())
