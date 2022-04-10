class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        need = {}
        for c in p:
            if c not in need.keys():
                need[c] = 0
            need[c] += 1

        window = {}
        valid = 0
        ans = []
        left = 0
        right = 0
        while right < len(s):
            c = s[right]
            # update status
            if c not in window.keys():
                window[c] = 0
            window[c] += 1
            if c in need.keys() and window[c] <= need[c]:
                valid += 1
            right += 1

            if right - left >= len(p):
                d = s[left]
                if valid == len(p):
                    ans.append(left)
                # update status
                if d in need.keys() and window[d] <= need[d]:
                    valid -= 1
                window[d] -= 1
                left += 1
        return ans


s = "cbaebabacd"
p = "abc"

s = "abab"
p = "ab"

#s = "a"
#p = "a"

solution = Solution()
print(solution.findAnagrams(s, p))
