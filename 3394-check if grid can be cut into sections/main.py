class Solution(object):
    def checkValidCuts(self, n, rectangles):
        """
        :type n: int
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        # pre-process
        horizontals = list()
        verticals = list()
        for rectangle in rectangles:
            horizontals.append((rectangle[0], rectangle[2]))
            verticals.append((rectangle[1], rectangle[3]))

        print(horizontals)
        print(verticals)

        # process
        # helper function
        def merge(intervals):
            intervals = sorted(intervals)
            start = intervals[0][0]
            limit = intervals[0][1]

            merges = list()
            for interval in intervals[1:]:
                if interval[0] < limit:
                    limit = max(limit, interval[1])
                else:
                    merges.append((start, limit))
                    start = interval[0]
                    limit = interval[1]
            merges.append((start, limit))

            if len(merges) >= 3:
                return True
            else:
                return False

        if merge(horizontals) or merge(verticals):
            return True
        else:
            return False


n = 5
rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]

n = 4
rectangles = [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]

n = 4
rectangles = [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]

n = 4
rectangles = [[0,0,1,4],[1,0,2,4],[2,0,3,4],[3,0,4,4]]

solution = Solution()
print(solution.checkValidCuts(n, rectangles))
