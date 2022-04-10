class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority, count = self.doMajorityElement(nums)
        return majority


    def doMajorityElement(self, nums):
        if len(nums) == 0:
            return None, 0
        elif len(nums) == 1:
            return nums[0], 1
        else:
            mid = len(nums) // 2
            left_majority, left_count = self.doMajorityElement(nums[:mid])
            right_majority, right_count = self.doMajorityElement(nums[mid:])

            if left_majority is None:
                return right_majority, right_count
            elif right_majority is None:
                return left_majority, left_count
            else:
                if left_majority == right_majority:
                    return left_majority, left_count + right_count
                else:
                    if left_count > right_count:
                        return left_majority, left_count - right_count
                    else:
                        return right_majority, right_count - left_count


solution = Solution()
nums = [3, 2, 3]
nums = [2, 2, 1, 1, 1, 2, 2]
nums = [6, 5, 5]
print(solution.majorityElement(nums))
