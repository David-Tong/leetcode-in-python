class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        N = 32
        M = 2 ** 31 - 1
        table = [0] * N
        for x in range(N):
            table[x] = 2 ** x + 1

        from bisect import bisect_left
        left_pos = bisect_left(table, right - left)
        if right - left == table[left_pos]:
            shift = left_pos + 1
        else:
            shift = left_pos

        mark = M << shift
        return left & right & mark

left = 5
right = 7

left = 0
right = 0

left = 1
right = 2147483647

left = 1996
right = 2022

left = 3000
right = 3860

left = 1
right = 2

left = 4
right = 7

left = 2
right = 3

solution = Solution()
print(solution.rangeBitwiseAnd(left, right))
