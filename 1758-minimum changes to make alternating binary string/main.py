class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        L = len(s)

        # keep the first digit
        keep = 0
        prev = s[0]
        for x in range(1, L):
            if s[x] == prev:
                prev = str(1 - int(s[x]))
                keep += 1
            else:
                prev = s[x]

        # swap the first digit
        swap = 1
        prev = str(1 - int(s[0]))
        for x in range(1, L):
            if s[x] == prev:
                prev = str(1 - int(s[x]))
                swap += 1
            else:
                prev = s[x]

        ans = min(keep, swap)
        return ans


s = "0100"
s = "10"
s = "1111"
s = "10010100"

solution = Solution()
print(solution.minOperations(s))
