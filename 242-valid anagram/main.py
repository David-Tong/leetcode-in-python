class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        from collections import defaultdict
        dicts = defaultdict(int)
        for ch in s:
            dicts[ch] += 1

        for ch in t:
            dicts[ch] -= 1

        for key in dicts:
            if dicts[key] > 0:
                return False
        return True


s = "anagram"
t = "nagaram"

s = "rat"
t = "car"

solution = Solution()
print(solution.isAnagram(s, t))
