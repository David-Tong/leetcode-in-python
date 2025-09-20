class Router(object):

    def __init__(self, memoryLimit):
        """
        :type memoryLimit: int
        """
        self.memoryLimit = memoryLimit
        self.memory = list()
        from collections import defaultdict
        self.dicts = defaultdict(bool)
        self.destinations = defaultdict(list)

    def addPacket(self, source, destination, timestamp):
        """
        :type source: int
        :type destination: int
        :type timestamp: int
        :rtype: bool
        """
        key = "{}-{}-{}".format(source, destination, timestamp)
        if key in self.dicts:
            return False
        if len(self.memory) == self.memoryLimit:
            self.forwardPacket()
        self.memory.append((source, destination, timestamp))
        self.destinations[destination].append(timestamp)
        self.dicts[key] = True
        return True


    def forwardPacket(self):
        """
        :rtype: List[int]
        """
        if self.memory:
            source, destination, timestamp = self.memory[0]
            key = "{}-{}-{}".format(source, destination, timestamp)
            del self.dicts[key]
            self.destinations[destination].pop(0)
            return self.memory.pop(0)
        else:
            return list()

    def getCount(self, destination, startTime, endTime):
        """
        :type destination: int
        :type startTime: int
        :type endTime: int
        :rtype: int
        """
        from bisect import bisect_left, bisect_right
        idx_start = bisect_left(self.destinations[destination], startTime)
        idx_end = bisect_right(self.destinations[destination], endTime)
        return idx_end - idx_start


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
# param_3 = obj.getCount(destination,startTime,endTime)
router = Router(3)
print(router.addPacket(1, 4, 90))
print(router.addPacket(2, 5, 90))
print(router.addPacket(1, 4, 90))
print(router.addPacket(3, 5, 95))
print(router.addPacket(4, 5, 105))
print(router.forwardPacket())
print(router.addPacket(5, 2, 110))
print(router.getCount(5, 100, 110))
print(router.getCount(5, 90, 110))
