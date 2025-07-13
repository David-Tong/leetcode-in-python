class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        evens, odds = defaultdict(int), defaultdict(int)
        for idx, ch in enumerate(s):
            if idx % 2 == 0:
                evens[ch] += 1
            else:
                odds[ch] += 1

        # print(evens)
        # print(odds)

        # process
        # case 1: put 1 in evens then 0 in odds
        ans = float("inf")
        if odds["1"] == evens["0"]:
            ans = odds["1"]

        # case 2: put 0 in evens then 1 in odds
        if odds["0"] == evens["1"]:
            ans = min(ans, odds["0"])

        return -1 if ans == float("inf") else ans


s = "111000"
s = "010"
s = "1110"

solution = Solution()
print(solution.minSwaps(s))
