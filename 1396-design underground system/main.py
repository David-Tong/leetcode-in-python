class UndergroundSystem(object):

    def __init__(self):
        from collections import defaultdict
        self.ids = defaultdict(list)
        self.averages = defaultdict(list)

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        if id not in self.ids:
            self.ids[id] = list()
            self.ids[id].append(list())
            self.ids[id].append(list())
        self.ids[id][0].append((stationName, t))

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.ids[id][1].append((stationName, t))
        idx = len(self.ids[id][1]) - 1
        start = self.ids[id][0][idx][0]
        end = self.ids[id][1][idx][0]
        time = self.ids[id][1][idx][1] - self.ids[id][0][idx][1]
        self.averages[start + ":" + end].append(time)

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        ans = sum(self.averages[startStation + ":" + endStation]) / float(len(self.averages[startStation + ":" + endStation]))
        return ans


us = UndergroundSystem()

"""
us.checkIn(45, "Leyton", 3)
us.checkIn(32, "Paradise", 8)
us.checkIn(27, "Leyton", 10)
us.checkOut(45, "Waterloo", 15)
us.checkOut(27, "Waterloo", 20)
us.checkOut(32, "Cambridge", 22)
print(us.getAverageTime("Paradise", "Cambridge"))
print(us.getAverageTime("Leyton", "Waterloo"))
us.checkIn(10, "Leyton", 24)
print(us.getAverageTime("Leyton", "Waterloo"))
us.checkOut(10, "Waterloo", 38)
print(us.getAverageTime("Leyton", "Waterloo"))
"""

us.checkIn(10, "Leyton", 3)
us.checkOut(10, "Paradise", 8)
print(us.getAverageTime("Leyton", "Paradise"))
us.checkIn(5, "Leyton", 10)
us.checkOut(5, "Paradise", 16)
print(us.getAverageTime("Leyton", "Paradise"))
us.checkIn(2, "Leyton", 21)
us.checkOut(2, "Paradise", 30)
print(us.getAverageTime("Leyton", "Paradise"))