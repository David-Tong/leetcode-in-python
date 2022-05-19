class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        index1 = 0
        nums3 = []
        while index1 < m:
            nums3.append(nums1[index1])
            index1 += 1

        index1 = 0
        index2 = 0
        index3 = 0
        while index3 < m and index2 < n:
            if nums3[index3] <= nums2[index2]:
                nums1[index1] = nums3[index3]
                index3 += 1
            else:
                nums1[index1] = nums2[index2]
                index2 += 1
            index1 += 1

        while index3 < m:
            nums1[index1] = nums3[index3]
            index3 += 1
            index1 += 1

        while index2 < n:
            nums1[index1] = nums2[index2]
            index2 += 1
            index1 += 1