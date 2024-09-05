class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        L = len(arr)
        intervals = list()

        for x in range(L):
            exist = False
            for y in range(L - 1, x, -1):
                if arr[y] < arr[x]:
                    interval = (x, y)
                    intervals.append(interval)
                    exist = True
                    break
            if not exist:
                interval = (x, x)
                intervals.append(interval)

        print(intervals)
        limit = intervals[0][1]
        ans = 1
        for interval in intervals[1:]:
            if interval[0] <= limit:
                pass
            else:
                ans += 1
            limit = max(limit, interval[1])
        return ans


arr = [4,3,2,1,0]
arr = [1,0,2,3,4]
arr = [7,6,1,2,3,4,0,5]
arr = [0,1,2,7,5,6,4,3]
#arr = [1,2,0,3]

solution = Solution()
print(solution.maxChunksToSorted(arr))
