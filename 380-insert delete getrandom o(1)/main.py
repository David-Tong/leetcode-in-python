class RandomizedSet(object):

    def __init__(self):
        from collections import defaultdict
        self.rset = defaultdict(int)

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.rset.keys():
            return False
        else:
            self.rset[val] = 1
            return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.rset:
            del self.rset[val]
            return True
        else:
            return False

    def getRandom(self):
        """
        :rtype: int
        """
        from random import randint
        keys = list(self.rset.keys())
        idx = randint(0, len(keys) - 1)
        return keys[idx]


rs = RandomizedSet()
print(rs.insert(1))
print(rs.remove(2))
print(rs.insert(2))
print(rs.getRandom())
print(rs.remove(1))
print(rs.insert(2))
print(rs.getRandom())