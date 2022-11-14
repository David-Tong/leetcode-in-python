class Pair(object):
    def __init__(self, frequency, word):
        self.frequency = frequency
        self.word = word

    def __lt__(self, other):
        if self.frequency == other.frequency:
            return self.word > other.word
        else:
            return self.frequency < other.frequency


class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        from collections import defaultdict
        dicts = defaultdict(int)
        for word in words:
            dicts[word] += 1

        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)
        for key in dicts:
            heappush(heap, Pair(dicts[key], key))
            while len(heap) > k:
                heappop(heap)

        ans = list()
        while heap:
            pair = heappop(heap)
            ans.append(pair.word)
        return ans[::-1]


words = ["i","love","leetcode","i","love","coding"]
k = 2

#words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
#k = 4

solution = Solution()
print(solution.topKFrequent(words, k))
