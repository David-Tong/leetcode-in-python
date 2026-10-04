class Solution(object):
    def findKthSmallest(self, coins, k):
        """
        :type coins: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(coins)

        # helper function
        # get lcm
        from fractions import gcd
        def getLcm(x, y):
            if x == 0 or y == 0:
                return 0
            return abs(x * y) // gcd(x, y)

        # bit count
        def countBit(combination):
            count = 0
            while combination:
                combination &= combination - 1
                count += 1
            return count

        # binary validate function
        def can(target):
            count = 0
            for combination in range(1, 1 << L):
                lcm = 1
                for idx, coin in enumerate(coins):
                    if combination >> idx & 1:
                        lcm = getLcm(lcm, coin)
                        if lcm > target:
                            break
                else:
                    """
                    print("-" * 50)
                    print(combination)
                    print(lcm)
                    print(countBit(combination))
                    print(target // lcm)
                    """
                    if countBit(combination) % 2 == 1:
                        count += target // lcm
                    else:
                        count -= target // lcm
            return count >= k

        # print(can(12))

        # process
        left, right = 1, min(coins) * k
        while left + 1 < right:
            middle = (left + right) // 2
            if can(middle):
                right = middle
            else:
                left = middle + 1

        if can(left):
            return left
        else:
            return right


coins = [3,6,9]
k = 3

coins = [5,2]
k = 7

from random import randint
coins = list(set([randint(2, 25) for _ in range(15)]))
k = 10 ** 9
print(coins)

solution = Solution()
print(solution.findKthSmallest(coins, k))
