class Solution(object):
    def maximumCoins(self, coins, k):
        """
        :type coins: List[List[int]]
        :type k: int
        :rtype: int
        """
        # pre-process
        coins.sort()
        lefts = []
        rights = []
        presums = [0]

        for left, right, coin in coins:
            lefts.append(left)
            rights.append(right)
            presums.append(presums[-1] + (right - left + 1) * coin)

        # print(lefts, rights, presums)

        # process
        # using binary search to find target during enumeration
        from bisect import bisect_left, bisect_right
        L = len(coins)
        ans = 0

        # step 1: enumerate from lefts
        for x in range(L):
            start = lefts[x]
            target = start + k - 1

            y = bisect_right(lefts, target) - 1
            if y < x:
                continue

            if target >= rights[y]:
                total = presums[y + 1] - presums[x]
            else:
                gap = rights[y] - target
                total = presums[y + 1] - presums[x] - gap * coins[y][2]

            ans = max(ans, total)

        # step 2: enumerate from rights
        for x in range(L):
            end = rights[x]
            target = end - k + 1
            if target <= 0:
                continue

            y = bisect_left(rights, target)
            if y >= L:
                continue

            if target <= lefts[y]:
                total = presums[x + 1] - presums[y]
            else:
                gap = target - lefts[y]
                total = presums[x + 1] - presums[y] - gap * coins[y][2]

            ans = max(ans, total)

        return ans


coins = [[8,10,1],[1,3,2],[5,6,4]]
k = 4

coins = [[1,10,3]]
k = 2

import random

def generate_test_data(n=None):
    # n = number of segments
    # default: random in valid range
    if n is None:
        n = random.randint(1, 10 ** 5)

    coins = []
    last = 0

    # coins
    for _ in range(n):
        # ensure non-overlapping by forcing left > last
        left = last + random.randint(1, 10 ** 3)  # random gap
        length = random.randint(1, 10 ** 3)       # segment length
        right = left + length - 1

        coin = random.randint(1, 10 ** 3)

        coins.append([left, right, coin])
        last = right

    # k can be huge
    k = random.randint(1, 10 ** 9)
    return coins, k

coins, k = generate_test_data()
print(coins)
print(k)

solution = Solution()
print(solution.maximumCoins(coins, k))
