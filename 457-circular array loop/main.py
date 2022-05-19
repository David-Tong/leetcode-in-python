class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.N = len(nums)
        self.visited = [False] * self.N
        self.loops = set()

        def checkCycle(nums, loop):
            # check if loop meets cycle requirement
            positive = False
            negative = False
            length = 0
            index = loop
            while True:
                if nums[index] > 0:
                    positive = True
                elif nums[index] < 0:
                    negative = True

                index += nums[index]
                if index < 0:
                    index += self.N
                index %= self.N

                length += 1
                if index == loop:
                    break

            if length > 1:
                return not (positive and negative)
            else:
                return False

        def checkCircle(nums, position):
            if position in self.visited:
                return

            # get the start of loop
            visited = []
            index = position
            while index not in visited:
                visited.append(index)
                index += nums[index]
                if index < 0:
                    index += self.N
                index %= self.N

            if not self.visited[index]:
                self.loops.add(index)

            for index in visited:
                self.visited[index] = True

        for idx in range(self.N):
            checkCircle(nums, idx)

        for loop in self.loops:
            if checkCycle(nums, loop):
                return True
        return False


nums = [2,-1,1,2,2]
#nums = [-1,2]
#nums = [-2,1,-1,-2,-2]
#nums = [1,-2,-1]
nums = [-1,-2,-3,-4,-5]
#nums = [2,2,2,2,2,4,7]

solution = Solution()
print(solution.circularArrayLoop(nums))
