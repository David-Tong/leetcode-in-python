class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        M = len(strs)
        N = len(strs[0])

        ans = 0
        for x in range(N):
            for y in range(M - 1):
                if strs[y][x] > strs[y + 1][x]:
                    ans += 1
                    break
        return ans


strs = ["cba","daf","ghi"]
strs = ["a","b"]
strs = ["zyx","wvu","tsr"]
strs = ["cba","caf","ghi"]

solution = Solution()
print(solution.minDeletionSize(strs))
