class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # convert
        digits = list()
        for ch in s:
            digits.append(str(ord(ch) - ord('a') + 1))
        d = "".join(digits)

        # transform
        for _ in range(k):
            total = 0
            for ch in d:
                total += int(ch)
            d = str(total)

        ans = int(d)
        return ans


s = "iiii"
k = 1

s = "leetcode"
k = 2

s = "zbax"
k = 2

solution = Solution()
print(solution.getLucky(s, k))