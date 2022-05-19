class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        N = n
        in_degrees = [0] * N
        out_degress = [0] * N

        for atrust in trust:
            out_degress[atrust[0] - 1] += 1
            in_degrees[atrust[1] - 1] += 1

        for x in range(N):
            if in_degrees[x] == N - 1 and out_degress[x] == 0:
                return x + 1
        return -1


n = 2
trust = [[1,2]]

n = 3
trust = [[1,3],[2,3]]

n = 3
trust = [[1,3],[2,3],[3,1]]

n = 1
trust = []

solution = Solution()
print(solution.findJudge(n, trust))
