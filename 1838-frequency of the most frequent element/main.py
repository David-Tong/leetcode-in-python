class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        L = len(nums)
        nums = sorted(nums)

        prefix = [0] * (L + 1)
        prefix[0] = 0
        for x in range(L):
            prefix[x + 1] = prefix[x] + nums[x]

        def doFrequency(target, nums, prefix, k):
            for x in range(target, L + 1):
                if (nums[x - 1] * target) - (prefix[x] - prefix[x - target]) <= k:
                    return True
            return False

        left = 1
        right = len(nums)

        while left + 1 < right:
            middle = (left + right) // 2
            if doFrequency(middle, nums, prefix, k):
                left = middle
            else:
                right = middle - 1

        if doFrequency(right, nums, prefix, k):
            return right
        else:
<<<<<<< HEAD
            return left


nums = [1,2,4]
k = 5

#nums = [1,4,8,13]
#k = 5

#nums = [3,9,6]
#k = 2

#nums = [1]
#k = 10000

#nums = [9930,9923,9983,9997,9934,9952,9945,9914,9985,9982,9970,9932,9985,9902,9975,9990,9922,9990,9994,9937,9996,9964,9943,9963,9911,9925,9935,9945,9933,9916,9930,9938,10000,9916,9911,9959,9957,9907,9913,9916,9993,9930,9975,9924,9988,9923,9910,9925,9977,9981,9927,9930,9927,9925,9923,9904,9928,9928,9986,9903,9985,9954,9938,9911,9952,9974,9926,9920,9972,9983,9973,9917,9995,9973,9977,9947,9936,9975,9954,9932,9964,9972,9935,9946,9966]
#k = 3056

#nums = [9926,9960,10000,9992,9917,9986,9934,9985,9977,9950,9922,9913,9971,9978,9984,9959,9934,9948,9918,9916,9967,9965,9985,9977,9988,9983,9900,9945,9913,9966,9968,9986,9939,9914,9980,9957,9921,9927,9917,9972,9974,9953,9984,9912,9975,9920,9966,9932,9921,9904,9928,9959,9993,9937,9934,9974,9937,9964,9922,9963,9991,9930,9944,9930,9982,9980,9967,9904,9955,9947,9924,9973,9997,9950,9905,9924,9990,9947,9953,9924,9977,9938,9951,9982,9932,9926,9928,9912,9917,9929,9924,9921,9987,9910,9927,9921,9929,9937,9919,9995,9949,9953]
#k = 3044

solution = Solution()
print(solution.maxFrequency(nums, k))
=======
            return left
>>>>>>> 8454ad0cbabb9eb52f0445fdebf643388dc21556
