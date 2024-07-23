class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        L = len(original)
        if m * n != L:
            return []

        ans = [[0] * n for _ in range(m)]

        idx = 0
        for x in range(m):
            for y in range(n):
                ans[x][y] = original[idx]
                idx += 1

        return ans


original = [1,2,3,4]
m = 2
n = 2

original = [1,2,3]
m = 1
n = 3

original = [1,2]
m = 1
n = 1

solution = Solution()
print(solution.construct2DArray(original, m, n))
