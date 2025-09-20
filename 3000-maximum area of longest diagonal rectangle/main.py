class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """
        # pre-process
        from math import sqrt
        maxi_diagnoal = 0
        idxes = list()
        for idx, dimension in enumerate(dimensions):
            diagnoal = sqrt(dimension[0] ** 2 + dimension[1] ** 2)
            if diagnoal > maxi_diagnoal:
                idxes = list()
                maxi_diagnoal = diagnoal
            if diagnoal == maxi_diagnoal:
                idxes.append(idx)

        # process
        ans = 0
        for idx in idxes:
            area = dimensions[idx][0] * dimensions[idx][1]
            ans = max(ans, area)
        return ans


dimensions = [[9,3],[8,6]]
dimensions = [[3,4],[4,3]]

solution = Solution()
print(solution.areaOfMaxDiagonal(dimensions))
