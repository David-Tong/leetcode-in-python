class AllOne(object):

    def __init__(self):
        from collections import defaultdict
        self.dicts = defaultdict(int)
        self.counts = defaultdict(set)
        self.maxi = -1
        self.mini = -1

    def inc(self, key):
        """
        :type key: str
        :rtype: None
        """
        if key in self.dicts:
            count = self.dicts[key]
        else:
            count = 0

        # update maxi
        if self.maxi == -1 or self.maxi == count:
            self.maxi = count + 1

        # update counts
        self.counts[count + 1].add(key)
        if count > 0:
            self.counts[count].remove(key)
        if len(self.counts[count]) == 0:
            del self.counts[count]

        # update mini
        if self.mini == -1 or self.mini == count:
            if count not in self.counts:
                self.mini = count + 1

        if count + 1 < self.mini:
            self.mini = count + 1

        # update dicts
        self.dicts[key] += 1

    def dec(self, key):
        """
        :type key: str
        :rtype: None
        """
        count = self.dicts[key]

        # update counts
        self.counts[count - 1].add(key)
        self.counts[count].remove(key)
        if len(self.counts[count]) == 0:
            del self.counts[count]

        # update mini
        if self.mini == count:
            if count == 1:
                if count not in self.counts[count]:
                    self.mini = -1
            else:
                self.mini -= 1

        # update maxi
        if self.maxi == count:
            if count not in self.counts:
                self.maxi -= 1

        # update dicts
        self.dicts[key] -= 1

    def getMaxKey(self):
        """
        :rtype: str
        """
        if self.maxi == -1:
            return ""
        else:
            item = self.counts[self.maxi].pop()
            self.counts[self.maxi].add(item)
            return item

    def getMinKey(self):
        """
        :rtype: str
        """
        if self.mini == -1:
            return ""
        else:
            item = self.counts[self.mini].pop()
            self.counts[self.mini].add(item)
            return item


"""
ao = AllOne()
ao.inc("hello")
ao.inc("hello")
print(ao.getMaxKey())
print(ao.getMinKey())
ao.inc("leet")
print(ao.getMaxKey())
print(ao.getMinKey())
ao.inc("leet")
ao.inc("leet")
ao.inc("leet")
ao.inc("leet")
ao.inc("leet")
print(ao.getMaxKey())
print(ao.getMinKey())
ao.dec("leet")
ao.dec("leet")
ao.dec("leet")
ao.dec("leet")
ao.dec("leet")
print(ao.getMaxKey())
print(ao.getMinKey())
"""

ao = AllOne()
ao.inc("a")
ao.inc("b")
ao.inc("b")
ao.inc("c")
ao.inc("c")
ao.inc("c")
ao.dec("b")
ao.dec("b")
print(ao.getMinKey())
ao.dec("a")
print(ao.getMaxKey())
print(ao.getMinKey())
