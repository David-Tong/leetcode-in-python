class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.length = length
        self.snaps = 0
        # self.elements[0][0] - list for snap versions
        # self.elements[0][1] - list for snap values
        self.elements = list()
        for _ in range(self.length):
            self.elements.append(list())
            self.elements[-1].append([0])
            self.elements[-1].append([0])

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if self.elements[index][0][-1] == self.snaps:
            self.elements[index][1][-1] = val
        else:
            self.elements[index][0].append(self.snaps)
            self.elements[index][1].append(val)

    def snap(self):
        """
        :rtype: int
        """
        self.snaps += 1

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        from bisect import bisect_left
        idx = bisect_left(self.elements[index][0], snap_id)
        if idx == len(self.elements[index][0]):
            return self.elements[index][1][idx - 1]
        else:
            if snap_id == self.elements[index][0][idx]:
                return self.elements[index][1][idx]
            else:
                return self.elements[index][1][idx - 1]


sa = SnapshotArray(3)
sa.set(0, 5)
sa.snap()
sa.set(0, 6)
sa.snap()
sa.snap()
sa.snap()
print(sa.get(0, 0))
print(sa.get(0, 3))
