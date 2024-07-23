class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        M = len(img)
        N = len(img[0])
        DIRECTION = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1))

        def doSmooth(x, y):
            from math import floor
            count, total = 0, 0
            for dx, dy in DIRECTION:
                if 0 <= x + dx < M and 0 <= y + dy < N:
                    count += 1
                    total += img[x + dx][y + dy]
            return int(floor(total * 1.0 / count))

        ans = [[0] * N for _ in range(M)]
        for x in range(M):
            for y in range(N):
                ans[x][y] = doSmooth(x, y)
        return ans


img = [[1,1,1],[1,0,1],[1,1,1]]
img = [[100,200,100],[200,50,200],[100,200,100]]
img = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

solution = Solution()
print(solution.imageSmoother(img))
