class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        segs = list()
        count = 1
        idx = 1
        while idx < len(s):
            if s[idx] != s[idx - 1]:
                segs.append(count)
                count = 1
            else:
                count += 1
            idx += 1
        segs.append(count)

        ans = 0
        idx = 1
        while idx < len(segs):
            ans += min(segs[idx], segs[idx - 1])
            idx += 1
        return ans


s = "00110011"
s = "10101"
s = "1"
s = "00000"

solution = Solution()
print(solution.countBinarySubstrings(s))
