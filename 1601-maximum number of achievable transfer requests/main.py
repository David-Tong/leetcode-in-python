class Solution(object):
    def maximumRequests(self, n, requests):
        """
        :type n: int
        :type requests: List[List[int]]
        :rtype: int
        """
        L = len(requests)

        def countOnes(mask):
            ones = 0
            while mask:
                if mask & 1:
                    ones += 1
                mask = mask >> 1
            return ones

        def canRequest(mask):
            from collections import defaultdict
            transfers = defaultdict(int)

            idx = 0
            while mask:
                if mask & 1:
                    transfer_out, transfer_in = requests[idx]
                    transfers[transfer_out] -= 1
                    transfers[transfer_in] += 1
                mask = mask >> 1
                idx += 1

            for key in transfers:
                if transfers[key] != 0:
                    return False
            return True

        from collections import defaultdict
        masks = defaultdict(list)

        for mask in range(2 ** L):
            ones = countOnes(mask)
            masks[ones].append(mask)

        for key in sorted(masks, key=lambda x: -x):
            for mask in masks[key]:
                if canRequest(mask):
                    return key
        return 0


n = 5
requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]

n = 3
requests = [[0,0],[1,2],[2,1]]

n = 4
requests = [[0,3],[3,1],[1,2],[2,0]]

n = 16
requests = [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,10],[10,11],[11,12],[12,13],[13,14],[14,15],[15,0]]

solution = Solution()
print(solution.maximumRequests(n, requests))
