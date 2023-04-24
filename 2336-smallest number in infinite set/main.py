class SmallestInfiniteSet(object):

    def __init__(self):
        self.pops = list()

    def popSmallest(self):
        """
        :rtype: int
        """
        if len(self.pops) == 0:
            smallest = 1
            self.pops.append(smallest)
        else:
            for x in range(len(self.pops)):
                if self.pops[x] > x + 1:
                    smallest = x + 1
                    self.pops = self.pops[:x] + [smallest] + self.pops[x:]
                    break
            else:
                smallest = self.pops[-1] + 1
                self.pops.append(smallest)
        return smallest

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num not in self.pops:
            return

        from bisect import bisect_left
        idx = bisect_left(self.pops, num)
        self.pops = self.pops[:idx] + self.pops[idx + 1:]


si = SmallestInfiniteSet()
si.addBack(2)
print(si.popSmallest())
print(si.popSmallest())
print(si.popSmallest())
si.addBack(1)
print(si.popSmallest())
print(si.popSmallest())
print(si.popSmallest())
si.addBack(2)
si.addBack(3)
print(si.popSmallest())
print(si.popSmallest())
print(si.popSmallest())
