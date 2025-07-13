class Solution(object):

    def __init__(self, m, n):
        """
        :type m: int
        :type n: int
        """
        self.M, self.N = m, n
        self.total = self.M * self.N
        self.ones = set()

    def flip(self):
        """
        :rtype: List[int]
        """
        import random
        idx = random.randint(0, self.total - 1)
        while idx in self.ones:
            idx = random.randint(0, self.total - 1)
        self.ones.add(idx)
        return self.__getCoordinator__(idx)

    def reset(self):
        """
        :rtype: None
        """
        self.ones = set()

    def __getCoordinator__(self, idx):
        x, y = idx // self.N, idx % self.N
        return x, y


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()

solution = Solution(3, 1)
# solution = Solution(10000, 10000)
print(solution.flip())
print(solution.flip())
print(solution.flip())
solution.reset()
print(solution.flip())
