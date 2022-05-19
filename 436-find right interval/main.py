class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        def findRight(lefts, target):
            left = 0
            right = len(lefts) - 1
            while left + 1 < right:
                middle = (left + right) // 2
                if lefts[middle][0] < target:
                    left = middle + 1
                else:
                    right = middle - 1
            if lefts[right][0] < target:
                return right + 1
            elif lefts[left][0] < target:
                return left + 1
            else:
                return left

        lefts = []
        rights = []
        for idx, interval in enumerate(intervals):
            lefts.append((interval[0], idx))
            rights.append(interval[1])

        lefts = sorted(lefts, key=lambda x: x[0])
        ans = [-1] * len(intervals)
        for idx, right in enumerate(rights):
            left_idx = findRight(lefts, right)
            if left_idx == len(lefts):
                ans[idx] = -1
            else:
                ans[idx] = lefts[left_idx][1]
        return ans


intervals = [[1,2]]
intervals = [[3,4],[2,3],[1,2]]
intervals = [[1,4],[2,3],[3,4]]
intervals = [[1,12],[2,9],[3,10],[13,14],[15,16],[16,17]]

solution = Solution()
print(solution.findRightInterval(intervals))
