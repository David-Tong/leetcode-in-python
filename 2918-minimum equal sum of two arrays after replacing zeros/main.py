class Solution(object):
    def minSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # pre-process
        zeros1, zeros2 = 0, 0
        total1, total2 = sum(nums1), sum(nums2)
        for num in nums1:
            if num == 0:
                zeros1 += 1
        for num in nums2:
            if num == 0:
                zeros2 += 1

        # process
        if zeros1 == zeros2 == 0:
            if total1 == total2:
                return total1
            else:
                return - 1
        elif zeros1 == 0:
            if total1 >= total2 + zeros2:
                return total1
            else:
                return -1
        elif zeros2 == 0:
            if total2 >= total1 + zeros1:
                return total2
            else:
                return -1
        else:
            return max(total1 + zeros1, total2 + zeros2)


nums1 = [3,2,0,1,0]
nums2 = [6,5,0]

nums1 = [2,0,2,0]
nums2 = [1,4]

nums1 = [2,5]
nums2 = [1,4]

solution = Solution()
print(solution.minSum(nums1, nums2))
