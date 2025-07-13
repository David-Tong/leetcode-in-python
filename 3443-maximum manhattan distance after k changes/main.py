class Solution(object):
    def maxDistance(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # pre-process
        DIRECTIONS = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}
        from collections import defaultdict
        dicts = defaultdict(int)

        # process
        ans = 0
        for d in s:
            dicts[d] += 1
            cx = min(dicts["E"], dicts["W"])
            cy = min(dicts["N"], dicts["S"])
            ans = max(ans, abs(dicts["E"] - dicts["W"]) + abs(dicts["N"] - dicts["S"]) + min(k, cx + cy) * 2)
        return ans

s = "NWSE"
k = 1

solution = Solution()
print(solution.maxDistance(s, k))