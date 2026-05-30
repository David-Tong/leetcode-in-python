class Solution(object):
    def minCost(self, s, cost):
        """
        :type s: str
        :type cost: List[int]
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(int)
        for idx, ch in enumerate(s):
            dicts[ch] += cost[idx]

        # process
        values = sorted(dicts.values())
        ans = sum(values[:-1])
        return ans


s = "aabaac"
cost = [1,2,3,4,1,10]

s = "abc"
cost = [10,5,8]

s = "zzzzz"
cost = [67, 67, 67, 67, 67]

solution = Solution()
print(solution.minCost(s, cost))
