class Solution(object):
    def smallestNumber(self, pattern):
        """
        :type pattern: str
        :rtype: str
        """
        # pre-process
        L = len(pattern) + 1

        # process
        # recursion function
        self.ans = ""
        def arrange(mask, result, step):
            if step == L:
                self.ans = result
                return True

            for x in range(L):
                if mask >> x & 1 == 0:
                    if step > 0:
                        if pattern[step - 1] == "I":
                            if result[-1] >= str(x + 1):
                                continue
                        elif pattern[step - 1] == "D":
                            if result[-1] <= str(x + 1):
                                continue
                    if arrange(mask | 1 << x, result + str(x + 1), step + 1):
                        return True

        arrange(0, "", 0)
        return self.ans


pattern = "IIIDIDDD"
pattern = "DDD"
pattern = "IIIIIDDI"

solution = Solution()
print(solution.smallestNumber(pattern))
