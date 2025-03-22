class NumberContainers(object):

    def __init__(self):
        from collections import defaultdict
        self.container = defaultdict(int)
        self.dicts = defaultdict(list)

    def change(self, index, number):
        """
        :type index: int
        :type number: int
        :rtype: None
        """
        from bisect import bisect_left

        # delete
        if index in self.container:
            old_number = self.container[index]
            idx = bisect_left(self.dicts[old_number], index)
            del self.dicts[old_number][idx]
            if len(self.dicts[old_number]) == 0:
                del self.dicts[old_number]

        # insert
        idx = bisect_left(self.dicts[number], index)
        self.dicts[number].insert(idx, index)
        self.container[index] = number

    def find(self, number):
        """
        :type number: int
        :rtype: int
        """
        return self.dicts[number][0] if number in self.dicts else -1


# Your NumberContainers object will be instantiated and called as such:
nc = NumberContainers()
print(nc.find(10))
nc.change(2, 10)
nc.change(1, 10)
nc.change(3, 10)
nc.change(5, 10)
print(nc.find(10))
nc.change(1, 20)
print(nc.find(10))
