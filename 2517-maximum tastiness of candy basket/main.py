class Solution(object):
    def maximumTastiness(self, price, k):
        """
        :type price: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(price)
        price = sorted(price)

        def validate(target):
            from bisect import bisect_right
            idx = 0
            nxt = price[0]
            while idx < k:
                if idx > 0:
                    nxt += target
                    idx2 = bisect_right(price, nxt)
                    if price[idx2 - 1] == nxt:
                        rest = L - idx2
                    else:
                        rest = L - 1 - idx2
                        if idx2 < L:
                            nxt = max(nxt, price[idx2])
                    expected_rest = k - 1 - idx
                    if rest < expected_rest:
                        return False

                idx += 1
            return True

        # process
        # print(validate(10))

        # binary search
        left, right = 0, 10 ** 9
        while left + 1 < right:
            middle = (left + right) // 2
            if validate(middle):
                left = middle
            else:
                right = middle - 1
        if validate(right):
            return right
        else:
            return left


price = [13,5,1,8,21,2]
k = 3

price = [1,3,1]
k = 2

price = [7,7,7,7]
k = 2

from random import randint
price = [randint(1,10 ** 5) for _ in range(10 ** 5)]
k = 1000
print(price)

solution = Solution()
print(solution.maximumTastiness(price, k))
