class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people = sorted(people, key=lambda x: (x[1], x[0]))
        results = []
        results.append(people[0])
        for ppl in people[1:]:
            count = 0
            length = len(results)
            index = length
            for x in range(length):
                if results[x][0] >= ppl[0]:
                    count += 1
                if count > ppl[1]:
                    index = x
                    break
            results.insert(index, ppl)
        return results


people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
people = [[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]
people = [[1, 0]]

solution = Solution()
print(solution.reconstructQueue(people))
