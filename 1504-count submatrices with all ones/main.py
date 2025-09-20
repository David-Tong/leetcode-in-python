class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        # pre-process
        M = len(mat)
        N = len(mat[0])

        # process
        # o(n ** 2) solution, find valid sub matrices with the bottom for a row
        hs = [0] * (N + 1)
        ans = 0
        for x in range(M):
            for y in range(N):
                hs[y + 1] = hs[y + 1] + 1 if mat[x][y] == 1 else 0
                # print(hs)

            # use monolithic stack to count valid sub matrices
            stack = list()
            stack.append(0)
            c = 0
            for y in range(N):
                while stack and hs[stack[-1]] > hs[y + 1]:
                    p1 = stack[-1]
                    stack.pop()
                    p2 = stack[-1]
                    c = c - (hs[p1] - hs[y + 1]) * (p1 - p2)
                stack.append(y + 1)
                c += hs[y + 1]
                ans += c
        return ans


mat = [[1,0,1],[1,1,0],[1,1,0]]
mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]

solution = Solution()
print(solution.numSubmat(mat))