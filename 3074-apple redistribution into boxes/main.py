class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        # pre-process
        L = len(capacity)
        total = sum(apple)

        # process
        capacity = sorted(capacity, reverse=True)
        idx = 0
        while total > 0:
           total -= capacity[idx]
           idx += 1
        ans = idx
        return ans


apple = [1,3,2]
capacity = [4,3,1,5,2]

apple = [5,5,5]
capacity = [2,4,2,7]

solution = Solution()
print(solution.minimumBoxes(apple, capacity))
