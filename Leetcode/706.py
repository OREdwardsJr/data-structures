class MyHashMap:

    def __init__(self):
        self.hash_map = []

    def __repr__(self): #Delete this
        return str(self.hash_map)

    def put(self, key: int, value: int) -> None:
        if self.hash_map == []:
            self.hash_map.append([key, value])
        else:
            for h_map in self.hash_map:
                if h_map[0] == key:
                    h_map[1] = value
                    return
            self.hash_map.append([key, value])

    def get(self, key: int) -> int:
        for h_map in self.hash_map:
            if h_map[0] == key:
                return h_map[1]
        return -1
        

    def remove(self, key: int) -> None:
        for h_map in self.hash_map:
            if h_map[0] == key:
                self.hash_map.remove(h_map)


obj = MyHashMap()
obj.put(1,1)
obj.put(2,5)
obj.put(2,3)
obj.put(100, 0)
print(obj)
print(obj.get(5))
obj.remove(1)
print(obj)



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)