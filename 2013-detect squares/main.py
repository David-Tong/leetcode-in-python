class DetectSquares(object):

    def __init__(self):
        from collections import defaultdict
        self.points = defaultdict(int)

    @staticmethod
    def __getkey__(x, y):
        return "{}-{}".format(x, y)

    @staticmethod
    def __getpoint__(key):
        return [int(_) for _ in key.split("-")]

    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        """
        x, y = point
        self.points[DetectSquares.__getkey__(x, y)] += 1

    def count(self, point):
        """
        :type point: List[int]
        :rtype: int
        """
        x, y = point
        ans = 0
        for key in self.points:
            ox, oy = DetectSquares.__getpoint__(key)
            if x != ox and y != oy:
                if abs(x - ox) == abs(y - oy):
                    key1 = DetectSquares.__getkey__(x, oy)
                    if key1 in self.points:
                        key2 = DetectSquares.__getkey__(ox, y)
                        if key2 in self.points:
                            ans += self.points[key] * self.points[key1] * self.points[key2]
        return ans


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)

"""
ds = DetectSquares()
ds.add([3, 10])
ds.add([11, 2])
ds.add([3, 2])
print(ds.count([11, 10]))
print(ds.count([14, 8]))
ds.add([11, 2])
print(ds.count([11, 10]))
ds.add([3,10])
print(ds.count([11, 10]))
ds.add([3,10])
print(ds.count([11, 10]))
ds.add([11, 10])
print(ds.count([11, 10]))
ds.add([1, 0])
ds.add([11, 0])
ds.add([1, 10])
print(ds.count([11, 10]))
ds.add([12, 11])
ds.add([12, 10])
ds.add([11, 11])
print(ds.count([11, 10]))
"""

ds = DetectSquares()
ds.add([5, 10])
ds.add([10, 5])
ds.add([3, 10])
print(ds.count([5, 5]))
ds.add([3, 0])
ds.add([8, 0])
ds.add([8, 5])
print(ds.count([3, 5]))
ds.add([9, 0])
ds.add([9, 8])
ds.add([1, 8])
print(ds.count([1, 0]))
ds.add([0, 0])
ds.add([8, 0])
ds.add([8, 8])
print(ds.count([0,8]))