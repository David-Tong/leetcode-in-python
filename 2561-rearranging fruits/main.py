class Solution(object):
    def minCost(self, basket1, basket2):
        """
        :type basket1: List[int]
        :type basket2: List[int]
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(dict)
        for cost in basket1:
            if cost not in dicts:
                dicts[cost] = [0] * 2
            dicts[cost][0] += 1
        for cost in basket2:
            if cost not in dicts:
                dicts[cost] = [0] * 2
            dicts[cost][1] += 1

        # print(dicts)
        mini = min(dicts.keys())

        dicts1, dicts2 = defaultdict(int), defaultdict(int)
        for cost in dicts:
            diff = abs(dicts[cost][0] - dicts[cost][1])
            if diff % 2 == 0:
                move = diff // 2
                if dicts[cost][0] > dicts[cost][1]:
                    dicts1[cost] = move
                elif dicts[cost][0] < dicts[cost][1]:
                    dicts2[cost] = move
            else:
                return -1
        if sum(dicts1.values()) != sum(dicts2.values()):
            return -1

        # print(dicts1)
        # print(dicts2)

        moves1, moves2 = list(), list()
        for key in sorted(dicts1.keys()):
            moves1.extend([key] * dicts1[key])
        for key in sorted(dicts2.keys()):
            moves2.extend([key] * dicts2[key])
        # print(moves1)
        # print(moves2)

        # process
        L = len(moves1)
        left1, left2 = 0, 0
        right1, right2 = L - 1, L - 1
        ans = 0
        for x in range(L):
            if 2 * mini <= min(moves1[left1], moves2[left2]):
                ans += 2 * mini
                right1 -= 1
                right2 -= 1
            else:
                if moves1[left1] <= moves2[left2]:
                    ans += moves1[left1]
                    left1 += 1
                    right2 -= 1
                else:
                    ans += moves2[left2]
                    left2 += 1
                    right1 -= 1
        return ans


basket1 = [4,2,2,2]
basket2 = [1,4,1,2]

basket1 = [2,3,4,1]
basket2 = [3,2,5,1]

basket1 = [2,2,1,1,1,1,1,2,2,1,1]
basket2 = [2,1,1,1,2,2,2,2,2,1,1]

basket1 = [84,80,43,8,80,88,43,14,100,88]
basket2 = [32,32,42,68,68,100,42,84,14,8]

basket1 = [84,84,1]
basket2 = [32,32,1]

solution = Solution()
print(solution.minCost(basket1, basket2))
