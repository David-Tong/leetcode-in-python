class AllOne(object):

    def __init__(self):
        from collections import defaultdict
        self.dicts = defaultdict(int)
        self.counts = defaultdict(set)
        self.maxi = float("-inf")
        self.mini = float("inf")

    def inc(self, key):
        """
        :type key: str
        :rtype: None
        """
        count = 0
        if key in self.dicts:
            count = self.dicts[key]
            self.counts[count].remove(key)
            if len(self.counts[count]) == 0:
                del self.counts[count]
                if count == self.mini:
                    self.mini = count + 1

        self.dicts[key] = count + 1
        self.counts[count + 1].add(key)
        self.maxi = max(self.maxi, count + 1)

    def dec(self, key):
        """
        :type key: str
        :rtype: None
        """
        count = self.dicts[key]
        self.counts[count].remove(key)
        if len(self.counts[count]) == 0:
            del self.counts[count]
            if count == self.mini:
                if count > 1:
                    self.mini = min(self.mini, count - 1)
                else:
                    if len(self.counts.keys()) == 0:
                        self.mini = float("inf")
                    else:
                        self.mini = min(self.counts.keys())


    def getMaxKey(self):
        """
        :rtype: str
        """


    def getMinKey(self):
        """
        :rtype: str
        """



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
#print(ao.getMaxKey())
#print(ao.getMinKey())
