class Solution(object):
    def rotateTheBox(self, box):
        """
        :type box: List[List[str]]
        :rtype: List[List[str]]
        """
        # pre-process
        M = len(box)
        N = len(box[0])

        # process
        ans = [["."] * M for _ in range(N)]
        for x in range(M):
            # split
            obstacles = [-1]
            stones = []
            stone = 0
            for y in range(N - 1, -1, -1):
                nx = N - 1 - y
                if box[x][y] == "*":
                    obstacles.append(nx)
                    stones.append(stone)
                    stone = 0
                elif box[x][y] == "#":
                    stone += 1
            stones.append(stone)
            print(obstacles, stones)

            # rearrange
            ny = M - 1 - x
            for obstacle_idx in range(len(obstacles)):
                start = N - 1 - obstacles[obstacle_idx]
                if 0 <= start < N:
                    nx = start
                    ans[nx][ny] = "*"
                for stone_idx in range(stones[obstacle_idx]):
                    nx = start - stone_idx - 1
                    ans[nx][ny] = "#"

        return ans


box = [["#",".","#"]]
box = [["#",".","*","."],
       ["#","#","*","."]]
box = [["#","#","*",".","*","."],
       ["#","#","#","*",".","."],
       ["#","#","#",".","#","."]]
box = [["#","#","*",".","*","."],
       ["#","#","#","*",".","."],
       ["#",".","*","#",".","*"]]
box = [["*"]]
box = [["*","#","*",".",".",".","#",".","*","."]]

solution = Solution()
print(solution.rotateTheBox(box))
