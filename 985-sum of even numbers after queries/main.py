class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        evens = 0
        odds = 0
        for num in nums:
            if num % 2 == 0:
                evens += num
            else:
                odds += num

        ans = list()
        for val, idx in queries:
            if nums[idx] % 2 == 0:
                evens -= nums[idx]
            else:
                odds -= nums[idx]

            change = val + nums[idx]
            if change % 2 == 0:
                evens += change
            else:
                odds += change

            nums[idx] = change
            ans.append(evens)
        return ans


nums = [1,2,3,4]
queries = [[1,0],[-3,1],[-4,0],[2,3]]

nums = [1]
queries = [[4,0]]

solution = Solution()
print(solution.sumEvenAfterQueries(nums, queries))
