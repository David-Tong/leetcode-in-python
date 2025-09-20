class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        # pre-process
        L = len(digits)

        # process
        numbers = set()
        for x in range(L):
            if digits[x] != 0:
                for y in range(L):
                    if x != y:
                        for z in range(L):
                            if x != z and y != z and digits[z] % 2 == 0:
                                number = str(digits[x]) + str(digits[y]) + str(digits[z])
                                numbers.add(number)
        ans = len(numbers)
        return ans


digits = [1,2,3,4]
digits = [0,2,2]
digits = [6,6,6]
digits = [1,3,5]
digits = [1,5,6,6,9,1,9,2,7]
digits = [0,9,6,1,4,7,0,1,3]

solution = Solution()
print(solution.totalNumbers(digits))

