class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        # pre-process
        L = len(arrays)
        maxis = list()
        for x in range(L):
            maxis.append(arrays[x][-1])
        maxis = sorted(maxis)

        # process
        ans = 0
        for x in range(L):
            mini = arrays[x][0]
            maxi = arrays[x][-1]
            if maxi == maxis[-1]:
                ans = max(ans, abs(maxis[-2] - mini))
            else:
                ans = max(ans, abs(maxis[-1] - mini))
        return ans


arrays = [[1,2,3],[4,5],[1,2,3]]
arrays = [[1],[1]]
arrays = [[1,2,3,4,5,7,8],[4,5]]

solution = Solution()
print(solution.maxDistance(arrays))
