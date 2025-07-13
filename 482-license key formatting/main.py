class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # pre-process
        cs = list()
        for c in s:
            if c != "-":
                if c.islower():
                    cs.append(c.upper())
                else:
                    cs.append(c)
        L = len(cs)

        # process
        splits = list()
        idx = k
        if L % k != 0:
            idx = L % k
        splits.append("".join(cs[:idx]))
        while idx < L:
            splits.append("".join(cs[idx:idx + k]))
            idx += k

        # post-process
        ans = "-".join(splits)
        return ans


s = "5F3Z-2e-9-w"
k = 4

s = "2-5g-3-J"
k = 2

solution = Solution()
print(solution.licenseKeyFormatting(s, k))
