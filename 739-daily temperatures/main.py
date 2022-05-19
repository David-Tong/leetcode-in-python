class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        N = len(temperatures)
        anses = [0] * N

        # stack - (idx, temperature)
        stack = list()
        for idx, temperature in enumerate(temperatures):
            while stack and stack[-1][1] < temperature:
                idx2, temperature2 = stack.pop()
                anses[idx2] = idx - idx2
            stack.append((idx, temperature))

        return anses


temperatures = [73,74,75,71,69,72,76,73]
temperatures = [30,40,50,60]
temperatures = [30,60,90]
temperatures = [15]
temperatures = [10,9,8,7,6,5,4,3,2,1]

solution = Solution()
print(solution.dailyTemperatures(temperatures))
