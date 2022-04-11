class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self, data: list):
        self.head = Node(data.pop(0))
        node = self.head
        for elem in data:
            node.next = Node(elem)
            node = node.next
    
    def __repr__(self) -> str:
        llstr = ""
        node = self.head
        while node:
            llstr += node.data + "->"
            node = node.next

        return llstr + "None"

    def insert(self, val, position: int) -> None:
        count = 0
        if position == 0:
            node = Node(val)
            node.next = self.head
            self.head = node
        else:
            node = self.head
            elem = Node(val)
            while node.next:
                if count == position:
                    elem.next = node
                    prev_node.next = elem
                    break
                prev_node = node
                node = node.next
                count += 1


    def delete(self, val) -> None:
        if self.head.data == val:
            self.head = self.head.next
            return
        else:
            node = self.head
            while node:
                if node.data == val:
                    previous_node.next = node.next
                    node.next = None
                    break
                previous_node = node
                node = node.next

    def search(self, val) -> bool:
        node = self.head
        while node:
            if node.data == val:
                return True
            node = node.next
        return False

    def merge(self, llist: object) -> None:
        #List1 -> List2
        node = self.head
        while node.next:
            node = node.next
        node.next = llist.head

countries = ["USA", "Canada", "Japan", "Mexico", "Brazil"]
country_ll = LinkedList(countries)
print(f"Original linked list: {country_ll}")

#insert
country_ll.insert("Peru", 2)
print(f"After adding Peru: {country_ll}")

#delete
country_ll.delete("Mexico")
print(f"After deleting Mexico: {country_ll}")

#search
#successful
print(f"USA is in linked list: {country_ll.search('USA')}")
#unsuccessful
print(f"Afghanistan is in linked list: {country_ll.search('Afghanistan')}")

#merge
new_countries = LinkedList(["Cuba", "Colombia", "Switzerland", "Ghana", "Thailand"])
country_ll.merge(new_countries)
print(f"After merger: {country_ll}")