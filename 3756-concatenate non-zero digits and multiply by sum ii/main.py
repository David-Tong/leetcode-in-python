class Solution(object):
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # pre-process
        MODULO = 10 ** 9 + 7
        L = len(s)

        # precompute powers of 10 modulo MODULO
        # pow10[k] = (10^k) % MODULO
        pow10 = [1] * (L + 1)
        for x in range(1, L + 1):
            pow10[x] = (pow10[x - 1] * 10) % MODULO

        # prefix arrays:
        # x_presums: sum of non-zero digits
        # sum_presums: concatenation of non-zero digits (modded)
        # cnt_presums: count of non-zero digits
        x_presums = [0]
        sum_presums = [0]
        cnt_presums = [0]

        for ch in s:
            num = int(ch)
            if num > 0:
                # add digit to x sum
                x_presums.append((x_presums[-1] + num) % MODULO)
                # append digit to concatenated number (modded)
                sum_presums.append((sum_presums[-1] * 10 + num) % MODULO)
                # increase count of non-zero digits
                cnt_presums.append(cnt_presums[-1] + 1)
            else:
                # zero digit: nothing changes
                x_presums.append(x_presums[-1])
                sum_presums.append(sum_presums[-1])
                cnt_presums.append(cnt_presums[-1])

        # process
        anses = []
        for left, right in queries:
            # sum of non-zero digits in range
            x = (x_presums[right + 1] - x_presums[left]) % MODULO
            # number of non-zero digits in this substring
            length = cnt_presums[right + 1] - cnt_presums[left]
            # reconstruct substring value using modular arithmetic
            sm = (sum_presums[right + 1] -
                  sum_presums[left] * pow10[length]) % MODULO
            anses.append((x * sm) % MODULO)
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
