class Solution(object):
    def findTheString(self, lcp):
        """
        :type lcp: List[List[int]]
        :rtype: str
        """
        # pre-process
        L = len(lcp)

        # process
        ans = [" "] * L

        import string
        idx = 0
        for ch in string.ascii_lowercase:
            while idx < L and ans[idx] != " ":
                idx += 1
            if idx == L:
                break
            idx2 = idx
            while idx2 < L:
                if lcp[idx][idx2] > 0:
                    ans[idx2] = ch
                idx2 += 1
        # print(ans)

        # validate
        # case 1 : we should not have any position not placed
        idx = 0
        while idx < L:
            if ans[idx] == " ":
                return ""
            idx += 1

        # case 2 : the generated ans should match lcs
        dp = [[0] * L for _ in range(L)]
        for x in range(L - 1, -1, -1):
            for y in range(L - 1, -1, -1):
                if ans[x] == ans[y]:
                    if x == L - 1 or y == L - 1:
                        dp[x][y] = 1
                    else:
                        dp[x][y] = dp[x + 1][y + 1] + 1
                if dp[x][y] != lcp[x][y]:
                    return ""

        ans = "".join(ans)
        return ans


lcp = [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]
# lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]]

solution = Solution()
print(solution.findTheString(lcp))
