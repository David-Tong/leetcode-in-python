class Node(object):

    def __init__(self, key, value, prev, next):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.size = 0
        self.capacity = capacity
        from collections import defaultdict
        self.dict = defaultdict(Node)
        self.head = Node(0, 0, None, None)
        self.rear = Node(0, 0, None, None)
        self.head.next = self.rear
        self.rear.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            curr = self.dict[key]
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            curr.prev = self.rear.prev
            self.rear.prev.next = curr
            self.rear.prev = curr
            curr.next = self.rear
            return curr.value
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dict:
            curr = self.dict[key]
            curr.value = value
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            curr.prev = self.rear.prev
            self.rear.prev.next = curr
            self.rear.prev = curr
            curr.next = self.rear
        else:
            if self.size == self.capacity:
                # evit
                delete = self.head.next
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
                del self.dict[delete.key]
                # append
            else:
                self.size += 1
            curr = Node(key, value, None, None)
            curr.prev = self.rear.prev
            self.rear.prev.next = curr
            self.rear.prev = curr
            curr.next = self.rear
            self.dict[key] = curr


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

'''
lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))
lru.put(3, 3)
print(lru.get(2))
lru.put(4, 4)
print(lru.get(1))
print(lru.get(3))
print(lru.get(4))
'''

lru = LRUCache(2)
lru.put(2, 1)
lru.put(2, 2)
print(lru.get(2))
lru.put(1, 1)
lru.put(4, 1)
print(lru.get(2))
