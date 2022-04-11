'''
• Add Child
• Search
• Traverse
    • In-order
    • Pre-order
    • Post-order
• Delete
• Find Max
• Find Min
'''

class BinarySearchTreeNode():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, val) -> None:
        if val == self.data:
            return 
        elif val < self.data:
            if self.left:
                self.left.add_child(val)
            else:
                self.left = BinarySearchTreeNode(val)
        elif val > self.data:
            if self.right:
                self.right.add_child(val)
            else:
                self.right = BinarySearchTreeNode(val)

    def search(self, val) -> bool:
        if val == self.data:
            return True
        elif val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        elif val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

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

    def delete(self, val) -> None:
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else: #val == self.data
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else: #self.left != None and self.right != None
                min_val = self.right.find_min()
                self.data = min_val
                self.right = self.right.delete(min_val)

        return self

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

def build_tree(data: list) -> object:
    root = BinarySearchTreeNode(data.pop(0))

    for elem in data:
        root.add_child(elem)

    return root

countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
country_tree = build_tree(countries)

print(f"Original list: {countries}")
print(f"In order traversal: {country_tree.in_order_traversal()}") #in order
print(f"Pre-order traversal: {country_tree.pre_order_traversal()}") #pre-order
print(f"Post-order traversal: {country_tree.post_order_traversal()}") #post-order

#add_child
country_tree.add_child('Canada')
print(f"Canada added to list: {country_tree.in_order_traversal()}") 


print(f"USA is in countries list: {country_tree.search('USA')}") #search - True
print(f"Japan is in countries list: {country_tree.search('Japan')}") #search - False
print(f"Country tree min: {country_tree.find_min()}") #find min
print(f"Country tree max: {country_tree.find_max()}") #find max

#delete
country_tree.delete("Canada")
print(f"Build tree after delete Canada: {country_tree.in_order_traversal()}")