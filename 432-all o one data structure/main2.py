class AllOne(object):

    def __init__(self):
        from collections import defaultdict
        self.dicts = defaultdict(int)

    def inc(self, key):
        """
        :type key: str
        :rtype: None
        """
        self.dicts[key] += 1

    def dec(self, key):
        """
        :type key: str
        :rtype: None
        """
        if self.dicts[key] > 1:
            self.dicts[key] -= 1
        else:
            del self.dicts[key]

    def getMaxKey(self):
        """
        :rtype: str
        """
        if len(self.dicts.keys()) == 0:
            return ""

        maxi = max(self.dicts.values())
        for key in self.dicts:
            if self.dicts[key] == maxi:
                return key

    def getMinKey(self):
        """
        :rtype: str
        """
        if len(self.dicts.keys()) == 0:
            return ""

        mini = min(self.dicts.values())
        for key in self.dicts:
            if self.dicts[key] == mini:
                return key


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
"""
