class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        def countOnes(num):
            ones = 0
            while num > 0:
                if num & 1 == 1:
                    ones += 1
                num >>= 1
            return ones

        def compare(num, num2):
            ones = countOnes(num)
            ones2 = countOnes(num2)

            if ones < ones2:
                return -1
            elif ones > ones2:
                return 1
            else:
                if num < num2:
                    return -1
                elif num > num2:
                    return 1
                else:
                    return 0

        from functools import cmp_to_key
        arr = sorted(arr, key=cmp_to_key(compare))
        return arr


arr = [0,1,2,3,4,5,6,7,8]
arr = [1024,512,256,128,64,32,16,8,4,2,1]

solution = Solution()
print(solution.sortByBits(arr))
