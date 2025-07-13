class Solution(object):
    def digArtifacts(self, n, artifacts, dig):
        """
        :type n: int
        :type artifacts: List[List[int]]
        :type dig: List[List[int]]
        :rtype: int
        """
        # pre-process
        M, N = 0, 0
        for artifact in artifacts:
            M = max(M, artifact[2])
            N = max(N, artifact[3])
        for d in dig:
            M = max(M, d[0])
            N = max(N, d[1])
        M, N = M + 1, N + 1
        # print(M, N)

        grid = [[False] * N for _ in range(M)]

        # helper function
        # extract
        def extract(artifact):
            sx, sy, ex, ey = artifact
            for x in range(sx, ex + 1):
                for y in range(sy, ey + 1):
                    if not grid[x][y]:
                        return False
            return True

        # process
        for d in dig:
            x, y = d
            # print(x, y)
            grid[x][y] = True

        ans = 0
        for artifact in artifacts:
            if extract(artifact):
                ans += 1
        return ans


n = 2
artifacts = [[0,0,0,0],[0,1,1,1]]
dig = [[0,0],[0,1]]

n = 2
artifacts = [[0,0,0,0],[0,1,1,1]]
dig = [[0,0],[0,1],[1,1]]

n = 6
artifacts = [[0,2,0,5],[0,1,1,1],[3,0,3,3],[4,4,4,4],[2,1,2,4]]
dig = [[0,2],[0,3],[0,4],[2,0],[2,1],[2,2],[2,5],[3,0],[3,1],[3,3],[3,4],[4,0],[4,3],[4,5],[5,0],[5,1],[5,2],[5,4],[5,5]]

n = 5
artifacts = [[0,0,0,0],[0,1,2,1],[3,1,3,4]]
dig = [[3,1],[3,2],[3,3],[3,4]]

solution = Solution()
print(solution.digArtifacts(n, artifacts, dig))
