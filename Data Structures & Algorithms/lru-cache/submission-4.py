"""
Approach:
Use a hash map for O(1) lookups
use a doubly linked list to maintain usage order in O(1)
keep least recently used item near the head and the most recently used near the tail
on get:
    return if it exists also move it to the right most place
on put:
    if the key is not there create it and add it to the right
    if the key is there remove from the place and add it to he right
"""

class Node:
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} #key -> Node
        
        #dummy head and tail to avoid edge case handling
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def insert(self, node):
        prev_right = self.right.prev
        prev_right.next = node
        node.prev = prev_right
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

