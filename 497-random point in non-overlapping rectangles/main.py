class Solution(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.rects = rects
        self.L = len(rects)
        self.presums = list()
        for idx in range(self.L):
            if idx == 0:
                self.presums.append(self.__area__(idx))
            else:
                self.presums.append(self.presums[-1] + self.__area__(idx))
        print(self.presums)
        self.total = self.presums[-1]

    def pick(self):
        """
        :rtype: List[int]
        """
        from random import randint
        select = randint(1, self.total)
        from bisect import bisect_left
        idx = bisect_left(self.presums, select)
        point = self.__random_point__(idx)
        return point

    def __random_point__(self, idx):
        from random import randint
        point = [randint(self.rects[idx][0], self.rects[idx][2]),
                 randint(self.rects[idx][1], self.rects[idx][3])]
        return point

    def __area__(self, idx):
        return ((self.rects[idx][2] - self.rects[idx][0] + 1)
                * (self.rects[idx][3] - self.rects[idx][1] + 1))


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()

# rects = [[-2, -2, 1, 1], [2, 2, 4, 6]]
rects = [[-2, -2, 1, 1], [2, 2, 2002, 2002]]
rects = [[82918473,-57180867,82918476,-57180863],[83793579,18088559,83793580,18088560],[66574245,26243152,66574246,26243153],[72983930,11921716,72983934,11921720]]
solution = Solution(rects)
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
