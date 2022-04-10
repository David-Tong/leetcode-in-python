class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        need = {}
        for c in s1:
            if c not in need.keys():
                need[c] = 0
            need[c] += 1

        left = 0
        right = 0
        window = {}
        valid = 0
        while right < len(s2):
            c = s2[right]
            # update window and valid info
            if c not in window.keys():
                window[c] = 0
            window[c] += 1
            if c in need.keys() and window[c] <= need[c]:
                valid += 1
            right += 1

            while right - left >= len(s1):
                if valid == len(s1):
                    return True
                d = s2[left]
                # update window and valid info
                if d in need.keys() and window[d] <= need[d]:
                    valid -= 1
                window[d] -= 1
                left += 1

        return False


solution = Solution()
s1 = "ab"
s2 = "eidbaooo"

s1 = "ab"
s2 = "eidboaoo"

print(solution.checkInclusion(s1, s2))
