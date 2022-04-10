class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def doPermutation(s, index, permutation):
            if len(s) == index:
                self.ans.append(permutation)
                return
            else:
                if s[index].isalpha():
                    doPermutation(s, index + 1, permutation + s[index].upper())
                    doPermutation(s, index + 1, permutation + s[index].lower())
                else:
                    doPermutation(s, index + 1, permutation + s[index])

        self.ans = []
        doPermutation(s, 0, "")
        return self.ans


s = "a1b2"
s = "3z4"

solution = Solution()
print(solution.letterCasePermutation(s))
