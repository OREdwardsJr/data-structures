class BSTNode:
    def __init__(self, elem=None) -> None:
        self.data = elem
        self.left = None
        self.right = None

    def add_child(self, val) -> None:
        if val == self.data:
            return
        elif val < self.data:
            if self.left:
                self.left.add_child(val)
            else:
                self.left = BSTNode(val)
        elif val > self.data:
            if self.right:
                self.right.add_child(val)
            else:
                self.right = BSTNode(val)

    def search(self, elem) -> bool:
        if elem == self.data:
            return True
        elif elem < self.data:
            if self.left:
                return self.left.search(elem)
            else:
                return False
        else:
            if self.right:
                return self.right.search(elem)
            else:
                return False

    def in_order_traversal(self) -> list:
        output = []

        if self.left:
            output += self.left.in_order_traversal()

        output.append(self.data)

        if self.right:
            output += self.right.in_order_traversal()

        return output

    def pre_order_traversal(self) -> list:
        output = [self.data]

        if self.left:
            output += self.left.pre_order_traversal()

        if self.right:
            output += self.right.pre_order_traversal()

        return output

    def post_order_traversal(self) -> list:
        output = []

        if self.left:
            output += self.left.post_order_traversal()

        if self.right:
            output += self.right.post_order_traversal()

        output.append(self.data)

        return output

    def delete_node(self, elem):
        if elem < self.data:
            self.left = self.left.delete_node(elem)
        elif elem > self.data:
            self.right = self.right.delete_node(elem)
        else:
            if not self.left and not self.right:
                return None
            elif not self.left:
                return self.right
            elif not self.right:
                return self.left
            else:
                min_val = self.right.find_min()
                self.data = min_val
                self.right.delete_node(min_val)

    def find_min(self):
        if not self.left:
            return self.data
        
        return self.left.find_min()

    def find_max(self):
        if not self.right:
            return self.data
        
        return self.right.find_max()

def build_tree(arr: list):
    root = BSTNode(arr.pop(0))

    for elem in arr:
        root.add_child(elem)

    return root

def find_height(node: BSTNode) -> int: #Recursive method Depth First Search
    if node == None:
        return 0

    l_height = find_height(node.left)
    r_height = find_height(node.right)

    return max(l_height, r_height) + 1

lst = [1, 20, 3, -3, 0, 100, 15, 23]
nums = build_tree(lst)
print(nums.in_order_traversal())
#print(nums.pre_order_traversal())
#print(nums.post_order_traversal())
#print(nums.find_min())
#print(nums.find_max())
#print(find_height(nums))