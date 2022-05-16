class BSTNode:
    def __init__(self, elem) -> None:
        self.data = elem
        self.left = None
        self.right = None

    def add_child(self, val) -> None:
        if self.data == val:
            return

        if val < self.data:
            if self.left:
                self.left.add_child(val)
            else:
                self.left = BSTNode(val)
        elif val > self.data:
            if self.right:
                self.right.add_child(val)
            else:
                self.right = BSTNode(val)

    def in_order_traversal(self) -> list:
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self) -> list:
        elements = [self.data]

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

    def level_order_traversal(self) -> list:
        q = [self]
        elements = []

        # Append Node to queue
        while q:

            # Pop Node from queue
            temp = q.pop(0)

            # Append Node.data to elements
            elements.append(temp.data)
            # Append Node.left
            if temp.left:
                q.append(temp.left)
            # Append Node.right
            if temp.right:
                q.append(temp.right)

        return elements

    def find_min(self) -> int | str:
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def find_max(self) -> int | str:
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def find_height(self, root) -> int:
        if not root:
            return 0

        l_depth = self.find_height(root.left)
        r_depth = self.find_height(root.right)

        return max(l_depth, r_depth) + 1

    def find(self, elem) -> bool:
        if elem == self.data:
            return True

        if elem < self.data:
            if self.left:
                return self.left.find(elem)
            else:
                return False

        if elem > self.data:
            if self.right:
                return self.right.find(elem)
            else:
                return False

    def delete(self, elem) -> None:
        if elem < self.data:
            if self.left:
                self.left = self.left.delete(elem)
        elif elem > self.data:
            if self.right:
                self.right = self.right.delete(elem)
        else:
            if not self.left and not self.right:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                min_val = self.right.find_min()
                self.data = min_val
                self.right = self.right.delete(min_val)

        return self

    def swap_nodes(self, elem1, elem2) -> None:
        pass


def build_tree(arr: list) -> BSTNode:
    root = BSTNode(arr.pop(0))

    for elem in arr:
        root.add_child(elem)

    return root


nums = [25, 20, 36, 10, 22, 30, 40, 12, 28, 5, 48, 38, 8, 45, 1, 50]
num_tree = build_tree(nums)

print(f"In order traversal: {num_tree.in_order_traversal()}")
print(f"Pre order traversal: {num_tree.pre_order_traversal()}")
print(f"Post order traversal: {num_tree.post_order_traversal()}")
print(f"Level order traversal: {num_tree.level_order_traversal()}")
print(f"Min node is: {num_tree.find_min()}")
print(f"Max node is: {num_tree.find_max()}")
print(f"Height of tree is: {num_tree.find_height(num_tree)}")
print(f"Searching for 20: {num_tree.find(20)}")
print(f"Searching for 200: {num_tree.find(200)}")
print(f"Delete 36 {num_tree.delete(36)}: {num_tree.in_order_traversal()}")
