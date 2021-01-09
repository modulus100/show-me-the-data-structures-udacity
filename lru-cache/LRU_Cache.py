class Node:

    def __init__(self, key, value, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev


class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key not in self.cache.keys():
            return -1

        node = self.cache[key]
        self.set(key, node.value)
        return node.value

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.head is None or self.capacity == 1:
            self.cache[key] = self.head = self.tail = Node(key, value)
        elif key in self.cache.keys():
            node = self.cache[key]
            if node is self.head:
                self.head.value = value
            else:
                node.prev.next = node.next
                self.head = Node(key, value, self.head)
                self.head.next.prev = self.head
                self.cache[key] = self.head
                if node is self.tail:
                    self.tail = node.prev
        elif len(self.cache) == self.capacity:
            self.head = Node(key, value, self.head)
            self.cache.pop(self.tail.key)
            self.tail = self.tail.prev
            self.cache[key] = self.head
        else:
            self.head = new_node = Node(key, value, self.head)
            new_node.next.prev = new_node
            self.cache[key] = self.head


our_cache = LRUCache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

our_cache.get(3)    # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
