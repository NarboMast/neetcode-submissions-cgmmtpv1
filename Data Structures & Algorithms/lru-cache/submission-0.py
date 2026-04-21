class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.nodes : Map(int, Node) = {}
        self.first, self.last = Node(-1,-1), Node(-1,-1)
        self.first.next, self.last.prev = self.last, self.first
        self.capacity = capacity

    def remove(self, curr):
        left = curr.prev
        right = curr.next
        left.next = right
        right.prev = left

    def insert(self, curr):
        prev = self.last.prev
        prev.next = curr
        curr.prev = prev
        curr.next = self.last
        self.last.prev = curr
        
    def get(self, key: int) -> int:
        if key in self.nodes:
            curr = self.nodes[key]
            self.remove(curr)
            self.insert(curr)
            return curr.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            self.remove(self.nodes[key])
        self.nodes[key] = Node(key, value)
        self.insert(self.nodes[key])

        if len(self.nodes) > self.capacity:
            temp = self.first.next
            self.remove(temp)
            del self.nodes[temp.key]
        