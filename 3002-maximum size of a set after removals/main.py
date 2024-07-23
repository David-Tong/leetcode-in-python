class Solution(object):
    def maximumSetSize(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # pre-process
        H = len(nums1) // 2

        set1 = set()
        for num1 in nums1:
            set1.add(num1)
        S1 = len(set1)

        set2 = set()
        for num2 in nums2:
            set2.add(num2)
        S2 = len(set2)

        intersection = set1.intersection(set2)
        I = len(intersection)

        # process
        if S1 > H:
            if I > S1 - H:
                I -= S1 - H
            else:
                I = 0
            S1 = H

        if S2 > H:
            if I > 0:
                if I > S2 - H:
                    I -= S2 - H
                else:
                    I = 0
            S2 = H

        return S1 + S2 - I


nums1 = [1,2,1,2]
nums2 = [1,1,1,1]

nums1 = [1,2,3,4,5,6]
nums2 = [2,3,2,3,2,3]

nums1 = [1,1,2,2,3,3]
nums2 = [4,4,5,5,6,6]

nums1 = [1,2,3,4,5,6]
nums2 = [1,2,3,4,5,6]

nums1 = [1,2,3,4,5,6]
nums2 = [7,8,9,10,11,12]

nums1 = [1,2,3,4,5,6]
nums2 = [1,1,2,2,3,3]

nums1 = [1,2,3,4,5,6]
nums2 = [1,2,3,4,5,7]

solution = Solution()
print(solution.maximumSetSize(nums1, nums2))
