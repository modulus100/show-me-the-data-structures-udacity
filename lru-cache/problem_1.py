"""
Solution is based on https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU and my
my solution which i used for leetcode. LRU cache can be implemented using a hashmap and a doubly linked list
HashMap as a key uses the key from get/set method and as a value it uses a reference to the node from doubly
linked list. Doubly linked list keeps nodes with value and works as a queue with limited capacity.
Overall complexity for get and set methods is O(1) (no iterative actions), space complexity is O(n), because
this cache stores max n nodes with values.
"""


class Node:
    """
    Doubly linked list implementation
    """

    def __init__(self, key, value, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev


class LRUCache(object):

    def __init__(self, capacity):
        if capacity < 1:
            raise Exception("Min size is 1")

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
        if key is None:
            raise Exception("key is invalid")
        if value is None:
            raise Exception("value is invalid")

        if self.cache_initialized():
            # if capacity is 1 or head is not initialized, then tail and head are the same
            self.cache[key] = self.head = self.tail = Node(key, value)
        elif key in self.cache.keys():
            # check if the key is already added
            node = self.cache[key]
            if node is self.head:
                # if the key at the top then we simply change a value
                self.head.value = value
            else:
                # move node from current position to the top
                node.prev.next = node.next
                self.head = Node(key, value, self.head)
                self.head.next.prev = self.head
                self.cache[key] = self.head

                # if the key at the tail then we set a new tail
                if node is self.tail:
                    self.tail = node.prev
        elif self.is_full():
            # simply adds a new head ant removes a tail
            self.head = Node(key, value, self.head)
            # removed from cache
            self.cache.pop(self.tail.key)
            self.tail = self.tail.prev
            self.cache[key] = self.head
        else:
            # simply adds an element to the queue
            self.head = new_node = Node(key, value, self.head)
            new_node.next.prev = new_node
            self.cache[key] = self.head

    def is_full(self) -> bool:
        return len(self.cache) == self.capacity

    def cache_initialized(self) -> bool:
        return self.head is None or self.capacity == 1


cache_size = 5
our_cache = LRUCache(cache_size)
print("cache size: " + str(cache_size))
print("set(1,1)")
our_cache.set(1, 1)
print("set(2,2)")
our_cache.set(2, 2)
print("set(3,3)")
our_cache.set(3, 3)
print("set(4,4)")
our_cache.set(4, 4)

res1 = our_cache.get(1)  # returns 1
print("get(1) expected val: 1, actual val: " + str(res1))
res2 = our_cache.get(2)  # returns 2
print("get(2) expected val: 2, actual val: " + str(res2))
res3 = our_cache.get(9)  # returns -1 because 9 is not present in the cache
print("get(9) expected val: -1, actual val: " + str(res3))

print("set(5,5)")
our_cache.set(5, 5)
print("set(6,6)")
our_cache.set(6, 6)

res4 = our_cache.get(3)  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print("get(3) expected val: -1, actual val: " + str(res4))

print()
print("Input validation")
try:
    our_cache.set(None, 1)
except Exception:
    print("throws exception for invalid key")

try:
    our_cache.set(1, None)
except Exception:
    print("throws exception for invalid value")

try:
    LRUCache(0)
except Exception:
    print("throws exception for invalid LRU cache init size")
