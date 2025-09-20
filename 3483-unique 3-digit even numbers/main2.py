class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        # process
        L = len(digits)
        self.numbers = set()

        from collections import defaultdict
        self.cache = defaultdict(bool)

        def dfs(idx, mask, number):
            key = "{}-{}-{}".format(idx, mask, number)
            if key in self.cache:
                return self.cache[key]

            if idx == 3:
                self.numbers.add(number)

            for x in range(L):
                if mask & 1 << x == 0:
                    if idx == 0:
                        if digits[x] == 0:
                            continue
                    elif idx == 2:
                        if digits[x] % 2 != 0:
                            continue
                    dfs(idx + 1, mask | 1 << x, number + str(digits[x]))
        dfs(0, 0, "")
        # print(self.numbers)
        ans = len(self.numbers)
        return ans


digits = [1,2,3,4]
digits = [0,2,2]
digits = [6,6,6]
digits = [1,3,5]
digits = [1,5,6,6,9,1,9,2,7]
digits = [0,9,6,1,4,7,0,1,3]

solution = Solution()
print(solution.totalNumbers(digits))
