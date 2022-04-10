class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        dicts = {}
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        for idx, ch in enumerate(pattern):
            if ch not in dicts:
                if words[idx] in dicts.values():
                    return False
                else:
                    dicts[ch] = words[idx]
            else:
                if words[idx] != dicts[ch]:
                    return False
        return True


pattern = "abba"
s = "dog cat cat dog"

pattern = "abba"
s = "dog cat cat fish"

pattern = "aaaa"
s = "dog cat cat dog"

solution = Solution()
print(solution.wordPattern(pattern, s))
