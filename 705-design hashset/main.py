class MyHashSet(object):

    def __init__(self):
        self.N = 10 ** 6 + 1
        self.nums = [0] * self.N

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.nums[key] = 1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.nums[key] = 0

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return self.nums[key] == 1


mhs = MyHashSet()
mhs.add(1)
mhs.add(2)
print(mhs.contains(1))
print(mhs.contains(3))
mhs.add(2)
print(mhs.contains(2))
mhs.remove(2)
print(mhs.contains(2))
