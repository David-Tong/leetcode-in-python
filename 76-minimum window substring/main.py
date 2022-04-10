class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            return ""

        need = {}
        for c in t:
            if c not in need.keys():
                need[c] = 0
            need[c] += 1

        window = {}
        left = 0
        right = 0
        valid = 0
        mini = len(s)
        ans = (0, 0)
        while right < len(s):
            c = s[right]
            # update status
            if c not in window.keys():
                window[c] = 0
            window[c] += 1
            if c in need.keys() and window[c] <= need[c]:
                valid += 1
            right += 1

            while valid >= len(t):
                # update answer
                if right - left <= mini:
                    mini = right - left
                    ans = (left, right)
                d = s[left]
                # update status
                if d in need.keys() and window[d] <= need[d]:
                    valid -= 1
                window[d] -= 1
                left += 1
        return s[ans[0]:ans[1]]


#S = "ADOBECODEBANC"
#T = "ABC"
S = "abc"
T = "cba"
S = "a"
T = "a"
S = "a"
T = "aa"
S = "aab"
T = "aab"
S = "cabwefgewcwaefgcf"
T = "cae"
sol = Solution()
print(sol.minWindow(S, T))
