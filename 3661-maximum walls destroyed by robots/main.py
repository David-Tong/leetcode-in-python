class Solution(object):
    def maxWalls(self, robots, distance, walls):
        """
        :type robots: List[int]
        :type distance: List[int]
        :type walls: List[int]
        :rtype: int
        """
        # pre-process
        L = len(robots)
        pairs = list()
        for x in range(L):
            pairs.append((robots[x], distance[x]))
        pairs = sorted(pairs)
        walls = sorted(walls)

        # print(pairs)
        # print(walls)

        # process
        # helper function
        # shoot(x, y) - the number of walls can be destroyed by the xth robot
        #             - shoots left for y = 0 or shoots right y = 1
        from bisect import bisect_left, bisect_right
        def shoot(x, y):
            if y == 0:
                idx = bisect_left(
                    walls, max(
                    float("-inf") if x == 0 else pairs[x - 1][0] + 1,
                    pairs[x][0] - pairs[x][1])
                )
                idx2 = bisect_right(walls, pairs[x][0])
            elif y == 1:
                idx = bisect_left(walls, pairs[x][0])
                idx2 = bisect_right(
                    walls, min(
                        float("inf") if x == L - 1 else pairs[x + 1][0] - 1,
                        pairs[x][0] + pairs[x][1])
                )
            return idx2 - idx

        # overlap(x) - the number of walls will be destroyed overlapped
        #            - if the xth robot shoot left and the x - 1 th robot shoot right
        def overlap(x):
            idx = bisect_left(walls, pairs[x - 1][0])
            idx2 = bisect_right(walls, pairs[x][0])
            return max(0, shoot(x - 1, 1) + shoot(x, 0) - (idx2 - idx))

        # dp init
        # dp[x][y] - the maximum walls can be destroyed by the xth robot
        #          - shoots left for y = 0 or shoots right y = 1
        dp = [[0] * 2 for _ in range(L)]
        dp[0][0] = shoot(0, 0)
        dp[0][1] = shoot(0, 1)

        # print(dp)

        # dp transfer
        # dp[x][0]
        for x in range(1, L):
            dp[x][0] = max(dp[x - 1][0] + shoot(x, 0), dp[x - 1][1] + shoot(x, 0) - overlap(x))
            dp[x][1] = max(dp[x - 1][1], dp[x - 1][0]) + shoot(x, 1)

        # print(dp)

        ans = max(dp[L - 1][0], dp[L - 1][1])
        return ans


robots = [4]
distance = [3]
walls = [1,10]

robots = [10,2]
distance = [5,1]
walls = [5,2,7]

robots = [1,2]
distance = [100,1]
walls = [10]

robots = [17,59,32,11,72,18]
distance = [5,7,6,5,2,10]
walls = [17,25,33,29,54,53,18,35,39,37,20,14,34,13,16,58,22,51,56,27,10,15,12,23,45,43,21,2,42,7,32,40,8,9,1,5,55,30,38,4,3,31,36,41,57,28,11,49,26,19,50,52,6,47,46,44,24,48]

from random import randint
robots = [randint(1, 20) for _ in range(5)]
distance = [randint(1, 10) for _ in range(5)]
walls = [randint(1, 100) for _ in range(5)]
print(robots)
print(distance)
print(walls)

solution = Solution()
print(solution.maxWalls(robots, distance, walls))
