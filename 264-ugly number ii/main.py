class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        from queue import PriorityQueue
        q = PriorityQueue()
        q.put(1)

        count = 0
        visited = set()
        while count < n:
            min = q.get()
            if not min in visited:
                count += 1
                visited.add(min)
                q.put(min * 2)
                q.put(min * 3)
                q.put(min * 5)

        return min


solution = Solution()
print(solution.nthUglyNumber(10))
print(solution.nthUglyNumber(1))
print(solution.nthUglyNumber(1690))
