class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        fives = 0
        tens = 0
        twenties = 0

        for bill in bills:
            if bill == 5:
                fives += 1
                continue
            elif bill == 10:
                if fives > 0:
                    tens += 1
                    fives -= 1
                else:
                    return False
            elif bill == 20:
                if tens > 0 and fives > 0:
                    tens -= 1
                    fives -= 1
                    twenties += 1
                elif fives > 2:
                    fives -= 3
                    twenties += 1
                else:
                    return False
        return True


bills = [5,5,5,10,20]
bills = [5,5,10,10,20]
bills = [5]

solution = Solution()
print(solution.lemonadeChange(bills))
