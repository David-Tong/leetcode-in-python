class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # pro-process
        L = len(s)

        left = 0
        right = 0

        # search
        ans = "1" * L
        ones = 0
        has = False
        while right < L:
            if s[right] == "1":
                ones += 1
            right += 1

            while ones > k:
                if s[left] == "1":
                    ones -= 1
                left += 1

            while left < L and s[left] == "0":
                left += 1

            if ones == k:
                has = True
                target = s[left:right]
                if len(target) < len(ans):
                    ans = target
                elif len(target) == len(ans):
                    if target < ans:
                        ans = target

        return ans if has else ""


s = "100011001"
k = 3

s = "1011"
k = 2

s = "000"
k = 1

s = "1110100001000100010110000110001"
k = 3

s = "11"
k = 2

solution = Solution()
print(solution.shortestBeautifulSubstring(s, k))
