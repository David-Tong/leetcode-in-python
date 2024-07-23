class Solution(object):
    def findFarmland(self, land):
        """
        :type land: List[List[int]]
        :rtype: List[List[int]]
        """
        # pre-process
        M = len(land)
        N = len(land[0])

        def doFind(start_x, start_y):
            # search vertical
            delta_x = 0
            end_x = start_x + delta_x
            while end_x < M and land[end_x][start_y] == 1:
                delta_x += 1
                end_x = start_x + delta_x
            end_x -= 1

            # search horizontal
            delta_y = 0
            end_y = start_y + delta_y
            while end_y < N and land[end_x][end_y] == 1:
                delta_y += 1
                end_y = start_y + delta_y
            end_y -= 1

            # mark searched
            for x in range(start_x, end_x + 1):
                for y in range(start_y, end_y + 1):
                    land[x][y] = 0

            return start_x, start_y, end_x, end_y

        # process
        ans = list()
        for x in range(M):
            for y in range(N):
                if land[x][y] == 1:
                    ans.append(doFind(x, y))
        return ans


land = [[1,0,0],[0,1,1],[0,1,1]]
land = [[1,1],[1,1]]
land = [[0]]

solution = Solution()
print(solution.findFarmland(land))
