class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        def doWin(total, round, mask):
            key = str(total) + "-" + str(round) + "-" + str(mask)
            if key in self.cache:
                return self.cache[key]

            for x in range(maxChoosableInteger - 1, -1, -1):
                # selected
                if mask >> x & 1:
                    pass
                else:
                    if total + x + 1 >= desiredTotal:
                        if round % 2 == 1:
                            self.cache[key] = False
                            return False
                        else:
                            self.cache[key] = True
                            return True
                    if round % 2 == 1:
                        if not doWin(total + x + 1, round + 1, (1 << x) | mask):
                            self.cache[key] = False
                            return False
                    else:
                        if doWin(total + x + 1, round + 1, (1 << x) | mask):
                            self.cache[key] = True
                            return True
            if round % 2 == 1:
                self.cache[key] = True
                return True
            else:
                self.cache[key] = False
                return False

        from collections import defaultdict
        self.cache = defaultdict(bool)

        total = sum(list(range(1, maxChoosableInteger + 1)))
        if total < desiredTotal:
            return False

        return doWin(0, 0, 0)


maxChoosableInteger = 10
desiredTotal = 11

maxChoosableInteger = 10
desiredTotal = 0

maxChoosableInteger = 10
desiredTotal = 1

maxChoosableInteger = 10
desiredTotal = 300

maxChoosableInteger = 10
desiredTotal = 40

maxChoosableInteger = 20
desiredTotal = 300

maxChoosableInteger = 4
desiredTotal = 6

solution = Solution()
print(solution.canIWin(maxChoosableInteger, desiredTotal))
