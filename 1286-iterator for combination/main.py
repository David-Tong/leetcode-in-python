class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.L = len(characters)
        self.characters = characters
        self.limit = 2 ** self.L
        self.CL = combinationLength
        self.__generate__()
        self.idx = 0
        self.C = len(self.combinations)

    def __generate__(self):
        self.combinations = list()
        target = 2 ** self.CL - 1
        while target < self.limit:
            if self.__valid__(target):
                self.combinations.append(self.__parse__(target))
            target += 1
        self.combinations = sorted(self.combinations)

    def __valid__(self, target):
        res = 0
        while target:
            if target & 1:
                res += 1
            if res > self.CL:
                return False
            target >>= 1
        return res == self.CL

    def __parse__(self, target):
        res = ""
        idx = 0
        while target:
            if target & 1:
                res += self.characters[idx]
            target >>= 1
            idx += 1
        return res

    def next(self):
        """
        :rtype: str
        """
        if self.idx < self.C:
            res = self.combinations[self.idx]
            self.idx += 1
            return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.idx < self.C


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()

characters = "abc"
combinationLength = 2

"""
characters = "abcdfghklmnpqrz"
combinationLength = 7
"""

itr = CombinationIterator(characters, combinationLength)
print(itr.next())
print(itr.hasNext())
print(itr.next())
print(itr.hasNext())
print(itr.next())
print(itr.hasNext())
"""
print(itr.next())
print(itr.hasNext())
print(itr.next())
print(itr.hasNext())
print(itr.next())
print(itr.hasNext())
print(itr.next())
print(itr.hasNext())
print(itr.next())
print(itr.hasNext())
"""
