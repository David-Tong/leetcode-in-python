class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict
        self.cache = defaultdict(str)

        def isPalindrome(ss):
            L = len(ss)
            if L % 2 == 1:
                left = L // 2
                right = L // 2
            else:
                left = L // 2 - 1
                right = L // 2

            while left >= 0 and right < L:
                if ss[left] != ss[right]:
                    return False
                left -= 1
                right += 1
            return True

        def cut(ss):
            if ss in self.cache:
                return self.cache[ss]

            if isPalindrome(ss):
                return 0

            L = len(ss)
            if L == 1:
                return 0

            ans = float("inf")
            for x in range(1, L):
                ans = min(ans, cut(ss[:x]) + cut(ss[x:]) + 1)
            self.cache[ss] = ans

            return ans

        return cut(s)


s = "aab"
s = "a"
s = "ab"
s = "abbabababababababb"
#s = "apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp"

solution = Solution()
print(solution.minCut(s))
