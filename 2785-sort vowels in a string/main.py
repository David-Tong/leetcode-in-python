class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # pre-process
        VOWELS = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        poses = list()
        vowels = list()
        for idx, ch in enumerate(s):
            if ch in VOWELS:
                poses.append(idx)
                vowels.append(ch)

        # replace
        vowels = sorted(vowels)
        idx = 0
        ans = list(s)
        for pos in poses:
            ans[pos] = vowels[idx]
            idx += 1
        return "".join(ans)


s = "lEetcOde"
s = "lYmpH"

solution = Solution()
print(solution.sortVowels(s))
