class Solution(object):
    def maxTotalFruits(self, fruits, startPos, k):
        """
        :type fruits: List[List[int]]
        :type startPos: int
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(fruits)
        init = 0
        idxes = map(lambda x: x[0], fruits)

        # process right
        from bisect import bisect_left, bisect_right
        idx = bisect_left(idxes, startPos)
        rights = [0]
        right_presum = [0]
        for x in range(idx, L):
            if fruits[x][0] - startPos > 0:
                rights.append(fruits[x][0] - startPos)
                right_presum.append(right_presum[-1] + fruits[x][1])
            elif fruits[x][0] - startPos == 0:
                init = fruits[x][1]

        print(rights)
        print(right_presum)

        # process left
        lefts = [0]
        left_presum = [0]
        for x in range(idx - 1, -1, -1):
            if startPos - fruits[x][0] > 0:
                lefts.append(startPos - fruits[x][0])
                left_presum.append(left_presum[-1] + fruits[x][1])

        print(lefts)
        print(left_presum)

        # process
        ans = 0
        for x in range(k):
            # case 1 : move left then right
            # move left first
            harvest = 0
            left = x
            idx = bisect_right(lefts, left)
            harvest += left_presum[idx - 1]
            # then move right
            right = k - 2 * left
            if right >= 0:
                idx = bisect_right(rights, right)
                harvest += right_presum[idx - 1]
            ans = max(ans, harvest)
            # print(left, right, ans)

            # case 2 : move right then left
            # move right first
            harvest = 0
            right = x
            idx = bisect_right(rights, right)
            harvest += right_presum[idx - 1]
            # then move left
            left = k - 2 * right
            if left >= 0:
                idx = bisect_right(lefts, left)
                harvest += left_presum[idx - 1]
            ans = max(ans, harvest)
            # print(left, right, ans)

        # post-process
        ans += init
        return ans


fruits = [[2,8],[6,3],[8,6]]
startPos = 5
k = 4

fruits = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]]
startPos = 5
k = 4

fruits = [[0,3],[6,4],[8,5]]
startPos = 3
k = 2

"""
from random import randint
fruits = list()
positions = set()
for _ in range(10 ** 4):
    position = randint(0, 2 * 10 ** 5)
    if position not in positions:
        fruits.append([position, randint(1, 10 ** 4)])
        positions.add(position)
fruits = sorted(fruits, key=lambda x: x[0])
startPos = randint(0, 2 * 10 ** 5)
k = 10000

print(fruits)
print(startPos)
"""

fruits = [[0,10000]]
startPos = 200000
k = 200000

solution = Solution()
print(solution.maxTotalFruits(fruits, startPos, k))
