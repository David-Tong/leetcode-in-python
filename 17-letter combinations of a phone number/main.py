class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.dicts = [[], [], ["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"], ["m", "n", "o"],
                      ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]]
        self.anses = []

        def doCombine(digits, ans):
            if len(digits) == 0:
                self.anses.append(ans)
                return

            for ch in self.dicts[int(digits[0])]:
                doCombine(digits[1:], ans + ch)

        if digits == "":
            return []

        doCombine(digits, "")
        return self.anses


digits = "23"
digits = ""
digits = "2"

solution = Solution()
print(solution.letterCombinations(digits))
