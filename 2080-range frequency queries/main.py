class RangeFreqQuery(object):

    def __init__(self, arr):
        """
        :type arr: List[int]
        """
        from collections import defaultdict
        self.dicts = defaultdict(list)
        for idx, num in enumerate(arr):
            self.dicts[num].append(idx)

    def query(self, left, right, value):
        """
        :type left: int
        :type right: int
        :type value: int
        :rtype: int
        """
        from bisect import bisect_left, bisect_right
        left_idx = bisect_left(self.dicts[value], left)
        right_idx = bisect_right(self.dicts[value], right)
        return right_idx - left_idx


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)

arr = [12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]
rfq = RangeFreqQuery(arr)
print(rfq.query(1 ,2 ,4))
print(rfq.query(0, 11, 33))
