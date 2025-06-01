class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(int)
        for digit in digits:
            dicts[digit] += 1

        # process
        self.ans = list(())
        # helper function
        def makeEvenNumbers(number, dicts, idx):
            for digit in dicts:
                if dicts[digit] > 0:
                    if idx == 1:
                        if digit % 2 == 0:
                            self.ans.append(int(number + str(digit)))
                    else:
                        if idx == 3 and digit == 0:
                            continue
                        dicts[digit] -= 1
                        makeEvenNumbers(number + str(digit), dicts, idx - 1)
                        dicts[digit] += 1
        makeEvenNumbers("", dicts, 3)
        ans = sorted(self.ans)
        return ans


digits = [2,1,3,0]
digits = [2,2,8,8,2]
digits = [3,7,5]

solution = Solution()
print(solution.findEvenNumbers(digits))
