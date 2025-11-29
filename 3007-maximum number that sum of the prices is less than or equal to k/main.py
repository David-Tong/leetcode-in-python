class Solution(object):
    def findMaximumNumber(self, k, x):
        """
        :type k: int
        :type x: int
        :rtype: int
        """
        # pre-process
        L = 50

        def can(target):
            target += 1
            idx = 0
            ones = 0
            while idx < L:
                if (idx + 1) % x == 0:
                    half = 2 ** idx
                    if target // half > 0:
                        base = 2 * half
                        ones += (target // base) * half
                        if (target // half) % 2 == 1:
                            ones += target % half
                        # print(ones)
                    else:
                        break
                idx += 1
            return True if ones <= k else False

        # print(can(9))
        # return

        left, right = 0, 10 ** 15
        while left + 1 < right:
            middle = (left + right) // 2
            if can(middle):
                left = middle
            else:
                right = middle - 1
        if can(right):
            return right
        else:
            return left


k = 9
x = 1

k = 7
x = 2

solution = Solution()
print(solution.findMaximumNumber(k, x))
