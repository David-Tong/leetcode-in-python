class Solution(object):
    def longestConsecutive(self, nums):
        length = len(nums)
        if length <= 1:
            return length

        book = dict()
        for i in range(length):
            if nums[i] not in book.keys():
                left = nums[i] - 1
                right = nums[i] + 1

                while left in book.keys():
                    left -= 1
                left += 1

                while right in book.keys():
                    right += 1
                right -= 1

                if left == right == nums[i]:
                    book[nums[i]] = 1
                elif left == nums[i]:
                    book[right] += 1
                    book[nums[i]] = book[right]
                elif right == nums[i]:
                    book[left] += 1
                    book[nums[i]] = book[left]
                else:
                    l = book[left] + book[right] + 1
                    book[nums[i]] = l
                    book[left] = l
                    book[right] = l
        return max(book.values())


nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
sol = Solution()
print(sol.longestConsecutive(nums))







