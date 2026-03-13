class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        # pre-process
        L = len(ranges)
        ranges = sorted(ranges)

        # process
        for x in range(left, right + 1):
            covered = False
            for y in range(L):
                if ranges[y][0] <= x <= ranges[y][1]:
                    covered = True
            if not covered:
                return False
        return True


ranges = [[1,2],[3,4],[5,6]]
left = 2
right = 5

ranges = [[1,10],[10,20]]
left = 21
right = 21

solution = Solution()
print(solution.isCovered(ranges, left, right))
