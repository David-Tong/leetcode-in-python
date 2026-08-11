class Solution(object):
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # pre-process
        MODULO = 10 ** 9 + 7
        x_presums = list()
        x_presums.append(0)
        sum_presums = list()
        sum_presums.append(0)

        for ch in s:
            num = int(ch)
            if num > 0:
                x_presum = (x_presums[-1] + num) % MODULO
                sum_presum = sum_presums[-1] * 10 + num
            else:
                x_presum = x_presums[-1]
                sum_presum = sum_presums[-1]
            x_presums.append(x_presum)
            sum_presums.append(sum_presum)
        print(x_presums)
        print(sum_presums)

        # process
        anses = list()
        for left, right in queries:
            x = x_presums[right + 1] - x_presums[left]
            l = len(str(sum_presums[right + 1])) - len(str(sum_presums[left]))
            sm = sum_presums[right + 1] - (sum_presums[left] * (10 ** l))
            print(x)
            print(sm)
            ans = x * sm % MODULO
            anses.append(ans)
        return anses


s = "10203004"
queries = [[0,7],[1,3],[4,6]]

"""
s = "1000"
queries = [[0,3],[1,1]]

s = "9876543210"
queries = [[0,9]]

s = "000000121"
queries = [[0,3],[1,1],[2,8]]

s = "035614"
queries = [[0,1]]
"""

"""
from string import digits
from random import choice, randint
s = "".join(choice(digits) for _ in range(10 ** 5))
queries = [[randint(0, 14749), randint(14750, 24749)] for _ in range(10 ** 5)]
# print(s)
print(queries)
"""

s = "42"
queries = [[0,0],[0,1],[1,1]]

solution = Solution()
print(solution.sumAndMultiply(s, queries))
