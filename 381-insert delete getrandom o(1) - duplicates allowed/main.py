class RandomizedCollection(object):

    def __init__(self):
        from collections import defaultdict
        self.dicts = defaultdict(list)
        self.items = list()

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        res = False
        if val not in self.dicts:
            res = True
        self.dicts[val].append(len(self.items))
        self.items.append((val, len(self.dicts[val]) - 1))
        return res

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        res = False
        if val in self.dicts:
            res = True
            # delete the last item in dicts
            idx = self.dicts[val][-1]
            self.dicts[val].pop()
            # swap
            if idx < len(self.items) - 1:
                self.items[idx] = self.items[-1]
                swapped_val = self.items[idx][0]
                swapped_idx = self.items[idx][1]
                self.dicts[swapped_val][swapped_idx] = idx
            self.items.pop()
            # del key if empty
            if len(self.dicts[val]) == 0:
                del self.dicts[val]

        return res

    def getRandom(self):
        """
        :rtype: int
        """
        from random import randint
        idx = randint(0, len(self.items) - 1)
        return self.items[idx][0]


rc = RandomizedCollection()
print(rc.insert(1))
print(rc.insert(1))
print(rc.insert(2))
print(rc.getRandom())
print(rc.remove(1))
print(rc.remove(1))
print(rc.remove(1))
print(rc.getRandom())

"""
rc = RandomizedCollection()
print(rc.insert(1))
print(rc.insert(1))
print(rc.remove(1))
print(rc.getRandom())
"""