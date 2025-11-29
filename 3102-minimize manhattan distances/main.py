class Solution(object):
    def minimumDistance(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # pre-process
        from sortedcontainers import SortedList
        sorted_lists = [SortedList() for _ in range(4)]

        for x, y in points:
            sorted_lists[0].add(x + y)
            sorted_lists[1].add(x - y)
            sorted_lists[2].add(-x + y)
            sorted_lists[3].add(x - y)

        # helper function
        # get maximum manhattan distance
        def max_md(sorted_lists):
            return max(sorted_lists[0][-1] - sorted_lists[0][0], max(
                sorted_lists[1][-1] - sorted_lists[1][0], max(
                    sorted_lists[2][-1] - sorted_lists[2][0],
                    sorted_lists[3][-1] - sorted_lists[3][0]
                )
            ))

        # process
        ans = float("inf")
        for x, y in points:
            # remove the point
            sorted_lists[0].remove(x + y)
            sorted_lists[1].remove(x - y)
            sorted_lists[2].remove(-x + y)
            sorted_lists[3].remove(x - y)

            ans = min(ans, max_md(sorted_lists))

            # add the point back
            sorted_lists[0].add(x + y)
            sorted_lists[1].add(x - y)
            sorted_lists[2].add(-x + y)
            sorted_lists[3].add(x - y)

        return ans


points = [[3,10],[5,15],[10,2],[4,4]]
points = [[1,1],[1,1],[1,1]]

solution = Solution()
print(solution.minimumDistance(points))
