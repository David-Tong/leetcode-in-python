class Solution(object):
    def maxNumberOfAlloys(self, n, k, budget, composition, stock, cost):
        """
        :type n: int
        :type k: int
        :type budget: int
        :type composition: List[List[int]]
        :type stock: List[int]
        :type cost: List[int]
        :rtype: int
        """
        def canCreate(target):
            for x in range(k):
                total = 0
                for y in range(n):
                    total += max(0, (target * composition[x][y] - stock[y]) * cost[y])
                    if total > budget:
                        break
                if total <= budget:
                    return True
            return False

        left = 0
        right = 10 ** 9

        while left + 1 < right:
            middle = (left + right) // 2
            if canCreate(middle):
                left = middle
            else:
                right = middle - 1

        if canCreate(right):
            return right
        else:
            return left


n = 3
k = 2
budget = 15
composition = [[1,1,1],[1,1,10]]
stock = [0,0,0]
cost = [1,2,3]

n = 3
k = 2
budget = 15
composition = [[1,1,1],[1,1,10]]
stock = [0,0,100]
cost = [1,2,3]

n = 2
k = 3
budget = 10
composition = [[2,1],[1,2],[1,1]]
stock = [1,1]
cost = [5,5]

n = 4
k = 9
budget = 55
composition = [[8,3,4,2],[3,9,5,5],[1,7,9,8],[7,6,5,1],[4,6,9,4],[6,8,7,1],[5,10,3,4],[10,1,2,4],[10,3,7,2]]
stock = [9,1,10,0]
cost = [3,4,9,9]

n = 1
k = 1
budget = 100000000
composition = [[1]]
stock = [83358995]
cost = [1]

solution = Solution()
print(solution.maxNumberOfAlloys(n, k, budget, composition, stock, cost))
