class BSTNode:
    def __init__(self, elem) -> None:
        self.data = elem
        self.left = None
        self.right = None

    def add_child(self, elem) -> None:
        if elem == self.data:
            return

        if elem < self.data:
            if self.left:
                self.left.add_child(elem)
            else:
                self.left = BSTNode(elem)

        if elem > self.data:
            if self.right:
                self.right.add_child(elem)
            else:
                self.right = BSTNode(elem)

    def search(self, elem) -> bool:
        if self.data == elem:
            return True

        if elem < self.data:
            if self.left:
                self.left.search(elem)
            else:
                return False

        if elem < self.data:
            if self.right:
                self.right.search(elem)
            else:
                return False

    def max_depth(self) -> int:
        if not self:
            return 0

        l_depth = self.left.max_depth()
        r_depth = self.right.max_depth()

        return max(l_depth, r_depth) + 1

    def in_order_traversal(self) -> list:
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self) -> list:
        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self) -> list:
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def level_order(self) -> list:
        elements = []

        # Use a Queue as q
        q = list()
        q.append(self)

        while q:
            print([qq.data for qq in q])
            # Pop node from q
            temp = q.pop(0)
            # Add node.data to arr: list
            elements.append(temp.data)
            # Add node.left
            if temp.left:
                q.append(temp.left)
            # Add node.right
            if temp.right:
                q.append(temp.right)

        return elements


def build_tree(arr: list) -> BSTNode:
    root = BSTNode(arr[0])

    for elem in arr:
        root.add_child(elem)

    return root


nums = [1, 2, 6, 29, -2, 0, 7]
num_tree = build_tree(nums)
print(f"{nums} as in order is {num_tree.in_order_traversal()}")
print(f"{nums} as level order is {num_tree.level_order()}")
