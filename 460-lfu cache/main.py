class Node(object):

    def __init__(self, key, value, count):
        self.key = key
        self.value = value
        self.count = count


class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        from collections import defaultdict
        from collections import OrderedDict

        self.capacity = capacity
        self.cache = defaultdict(Node)
        self.counter = defaultdict(OrderedDict)
        self.mini = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # delete the node from counter
        del self.counter[node.count][key]
        if not self.counter[node.count]:
            del self.counter[node.count]

        # count++
        node.count += 1

        # insert the node back to counter
        self.counter[node.count][key] = node

        if self.mini not in self.counter:
            self.mini += 1

        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.capacity > 0:
            # update
            if key in self.cache:
                self.cache[key].value = value
                self.get(key)
            else:
                # evict least frequently used cache
                if len(self.cache) == self.capacity:
                    k, _ = self.counter[self.mini].popitem(last=False)
                    del self.cache[k]
                    if not self.counter[self.mini]:
                        del self.counter[self.mini]

                # insert
                node = Node(key, value, 1)
                self.cache[key] = node
                self.counter[node.count][key] = node
                self.mini = 1


lfu = LFUCache(2)
lfu.put(3, 1)
lfu.put(2, 1)
lfu.put(2, 2)
lfu.put(4, 4)
lfu.get(2)
