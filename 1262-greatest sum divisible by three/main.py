class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        ones = list()
        twos = list()
        total = 0
        for num in nums:
            if num % 3 == 1:
                ones.append(num)
            elif num % 3 == 2:
                twos.append(num)
            total += num

        ones = sorted(ones)
        twos = sorted(twos)

        # process
        if total % 3 == 1:
            if len(ones) > 0 and len(twos) > 1:
                if ones[0] <= twos[0] + twos[1]:
                    return total - ones[0]
                else:
                    return total - twos[0] - twos[1]
            elif len(ones) > 0:
                return total - ones[0]
            elif len(twos) > 1:
                return total - twos[0] - twos[1]
            else:
                return 0
        elif total % 3 == 2:
            if len(ones) > 1 and len(twos) > 0:
                if ones[0] + ones[1] <= twos[0]:
                    return total - ones[0] - ones[1]
                else:
                    return total - twos[0]
            elif len(ones) > 1:
                return total - ones[0] - ones[1]
            elif len(twos) > 0:
                return total - twos[0]
            else:
                return 0
        else:
            return total


nums = [3,6,5,1,8]
nums = [4]
nums = [1,2,3,4,4]
nums = [1,2,5,3,11,2,3,45,6,1,22,678,9,8,11,7]
nums = [3,6,9]

solution = Solution()
print(solution.maxSumDivThree(nums))
