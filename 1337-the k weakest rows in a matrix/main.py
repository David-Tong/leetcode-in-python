class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        rows = []
        for idx, row in enumerate(mat):
            rows.append((sum(row), idx))

        rows = sorted(rows)
        ans = []
        for row in rows[:k]:
            ans.append(row[1])
        return ans


mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]
k = 3

mat = [[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]]
k = 2

solution = Solution()
print(solution.kWeakestRows(mat, k))
