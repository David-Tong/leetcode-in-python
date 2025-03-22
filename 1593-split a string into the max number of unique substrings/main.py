class Solution(object):
    def maxUniqueSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        # pre-process
        L = len(s)
        # use binary to represent a split plan
        # s = "xxxxxx"
        # binary = 10100
        # split plan : "x" "xx" "xxx"

        # process
        ans = 1
        for binary in range(2 ** L):
            splits = [-1]
            subs = set()
            for x in range(L):
                if binary >> x & 1:
                    splits.append(x)
            splits.append(L)

            if binary == 70:
                pass

            valid = True
            for x in range(1, len(splits)):
                sub = s[splits[x - 1] + 1: splits[x] + 1]
                if sub not in subs:
                    if sub:
                        subs.add(sub)
                else:
                    valid = False
                    break

            if valid:
                ans = max(ans, len(subs))
        return ans


s = "ababccc"
s = "aba"
s = "aa"
s = "abbababababbcccc"

solution = Solution()
print(solution.maxUniqueSplit(s))
