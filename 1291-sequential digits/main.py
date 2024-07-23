class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        # pre-process
        L = len(str(low))
        H = len(str(high))

        # enumerate
        sequence = list()
        for x in range(L, H + 1):
            for y in range(1, 10):
                if y + x <= 10:
                    digit = str(y)
                    for z in range(1, x):
                        digit += str(y + z)
                    sequence.append(int(digit))

        # process
        print(sequence)
        return filter(lambda x: x >= low and x <= high, sequence)


low = 100
high = 300

low = 1000
high = 13000

solution = Solution()
print(solution.sequentialDigits(low, high))
