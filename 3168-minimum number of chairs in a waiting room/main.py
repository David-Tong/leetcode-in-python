class Solution(object):
    def minimumChairs(self, s):
        """
        :type s: str
        :rtype: int
        """
        # process
        count = 0
        ans = 0
        for ch in s:
            if ch == "E":
                count += 1
            elif ch == "L":
                count -= 1
            ans = max(ans, count)
        return ans


s = "EEEEEEE"
s = "ELELEEL"
s = "ELEELEELLL"

solution = Solution()
print(solution.minimumChairs(s))
