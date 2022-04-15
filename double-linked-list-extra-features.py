'''
Double-linked list with numerous features
'''

class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class LinkedList():
    def __init__(self, data: list) -> None:
        self.head = Node(data.pop(0))
        self.length = 1
        node = self.head
        #Fill self.right
        for elem in data:
            node.right = Node(elem)
            node = node.right
            self.length += 1
        #Fill self.left
        node = self.head
        for elem in data[::-1]:
            node.left = Node(elem)
            node = node.left

    def __repr__(self) -> str:
        llstr = "<->"
        node = self.head
        while node:
            llstr += node.data + "<->"
            node = node.right
        return llstr

    def __iter__(self) -> str:
        node = self.head
        while node:
            yield node.data
            node = node.right

    def add_child(self, position: int, val):
        node = self.head
        self.length += 1
        new_node = Node(val)
        count = 0
        if position == 0:
            pass #new head
        while node:
            if count == position - 1:
                new_node = Node(val)
                new_node.left = node
                new_node.right = node.right
                node.right.left = new_node
                node.right = new_node
                return
            node = node.right
            count += 1

    def add_items(self, position: int, data:list):
        pass

    def delete(self, val):
        self.length -= 1
        pass
    
    def forward_traversal(self) -> str:
        node = self.head
        llstr = ""
        while node:
            llstr += node.data + "->"
            node = node.right
        return llstr 

    def backward_traversal(self) -> str:
        node = self.head
        llstr = ""
        while node:
            llstr += node.data + "->"
            node = node.left
        return llstr 

    def search(self, val) -> bool:
        node = self.head
        while node:
            if val == node.data:
                return True
            else:
                node = node.right
        return False
        
    def find_index(self, index) -> int:
        count = 0
        node = self.head
        while node:
            if count == index:
                return node.data
            node = node.right
        return "Invalid search entry"

    def min_value(self):
        node = self.head
        min_val = node.data
        while node:
            if node.data < min_val:
                min_val = node.data
        return min_val

    def max_value(self):
        node = self.head
        max_val = node.data
        while node:
            if node.data > max_val:
                max_val = node.data
        return max_val

    def mid_value(self):
        count = 0
        node = self.head
        while node:
            if count == self.length // 2:
                return node.data
            node = node.right
            count += 1

    def merge(self):
        pass

nba_teams = ["Cavaliers", "Jazz", "Suns", "Lakers", "Heat", "Clippers", "Bucks"]
nba_list = LinkedList(nba_teams)
'''
print(f"Forward traversal: {nba_list.forward_traversal()}")
print()
print(f"Backward traversal: {nba_list.backward_traversal()}")
print()
'''
#print(nba_list)
'''
nba_list.add_child(2, "Hornets")
print(f"Linked list {nba_list} - length: {nba_list.length}")
'''

print(nba_list.mid_value())