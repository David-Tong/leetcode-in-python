# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        def rand7():
            from random import randint
            return randint(1, 7)

        BASE = 7
        BOUND = 40

        while True:
            total = (rand7() - 1) * BASE + rand7()
            if total > BOUND:
                pass
            else:
                if total % 10 == 0:
                    return 10
                else:
                    return total % 10


n = 100

solution = Solution()
for x in range(n):
    print(solution.rand10())
