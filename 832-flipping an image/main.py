class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        # pre-process
        M = len(image)
        N = len(image[0])

        # process
        ans = [[0] * N for _ in range(M)]

        # flip the image horizontally
        for x in range(M):
            for y in range(N):
                ans[x][y] = image[x][N - 1 - y]

        # invert it
        for x in range(M):
            for y in range(N):
                ans[x][y] = 1 - ans[x][y]

        return ans


image = [[1,1,0],[1,0,1],[0,0,0]]

solution = Solution()
print(solution.flipAndInvertImage(image))
