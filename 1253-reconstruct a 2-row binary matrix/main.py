class Solution(object):
    def reconstructMatrix(self, upper, lower, colsum):
        """
        :type upper: int
        :type lower: int
        :type colsum: List[int]
        :rtype: List[List[int]]
        """
        M = 2
        N = len(colsum)

        ans = [[0] * N for _ in range(M)]
        for x in range(N):
            if colsum[x] == 2:
                # must put one in upper
                if upper == 0:
                    return list()
                upper -= 1
                ans[0][x] = 1
                # put one in lower
                if lower == 0:
                    return list()
                lower -= 1
                ans[1][x] = 1
            elif colsum[x] == 1:
                # try to put one in max(upper, lower)
                if upper >= lower:
                    # put one in upper
                    if upper == 0:
                        return list()
                    upper -= 1
                    ans[0][x] = 1
                else:
                    # put one in lower
                    if lower == 0:
                        return list()
                    lower -= 1
                    ans[1][x] = 1
        if upper == 0 and lower == 0:
            return ans
        else:
            return list()


upper = 2
lower = 1
colsum = [1,1,1]

upper = 2
lower = 3
colsum = [2,2,1,1]

upper = 5
lower = 5
colsum = [2,1,2,0,1,0,1,2,0,1]

upper = 4
lower = 7
colsum = [2,1,2,2,1,1,1]

solution = Solution()
print(solution.reconstructMatrix(upper, lower, colsum))
