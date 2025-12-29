class Solution(object):
    def maxSumDistinctTriplet(self, x, y):
        """
        :type x: List[int]
        :type y: List[int]
        :rtype: int
        """
        # pre-process
        L = len(x)

        from collections import defaultdict
        dicts = defaultdict(int)
        idx = 0
        while idx < L:
            if x[idx] not in dicts:
                dicts[x[idx]] = y[idx]
            else:
                dicts[x[idx]] = max(dicts[x[idx]], y[idx])
            idx += 1
        # print(dicts)

        # process
        if len(dicts) < 3:
            return -1
        else:
            return sum(sorted(dicts.values())[-3:])


x = [1,2,1,3,2]
y = [5,3,4,6,2]

x = [1,2,1,2]
y = [4,5,6,7]

x = [19,15,7,13]
y = [13,11,13,11]

solution = Solution()
print(solution.maxSumDistinctTriplet(x, y))
