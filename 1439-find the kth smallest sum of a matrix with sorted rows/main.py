class Solution(object):
    def kthSmallest(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: int
        """
        # pre-process
        M = len(mat)
        N = len(mat[0])

        # process
        # the intuition is to keep only smallest k temporary calculation results
        minis = [0]
        for x in range(M):
            temp = list()
            for mini in minis:
                for y in range(N):
                    temp.append(mini + mat[x][y])
            # print(temp)
            minis = sorted(temp)[:k]
        ans = minis[k - 1]
        return ans


mat = [[1,3,11],[2,4,6]]
k = 5

mat = [[1,3,11],[2,4,6]]
k = 9

mat = [[1,10,10],[1,4,5],[2,3,6]]
k = 7

solution = Solution()
print(solution.kthSmallest(mat, k))
