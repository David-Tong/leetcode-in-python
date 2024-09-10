class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        N = len(tasks)

        for idx, task in enumerate(tasks):
            task.append(idx)
        tasks = sorted(tasks, key=lambda x: x[0])
        print(tasks)

        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)
        offset = tasks[0][0]

        idx = 0
        processed = 0
        ans = list()
        while processed < N:
            # pop task
            if heap:
                processed_time, task_id = heappop(heap)
                offset += processed_time
                print("offset - {}, processed task - {}".format(offset, task_id))
                ans.append(task_id)
                processed += 1

            # push tasks
            while idx < N and tasks[idx][0] <= offset:
                heappush(heap, (tasks[idx][1], tasks[idx][2]))
                idx += 1

            # or push task
            if not heap and idx < N:
                offset = tasks[idx][0]

            while idx < N and tasks[idx][0] <= offset:
                heappush(heap, (tasks[idx][1], tasks[idx][2]))
                idx += 1
        return ans


tasks = [[1,2],[2,4],[3,2],[4,1]]
tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
tasks = [[1,2],[7,12],[100,25],[100,10]]
tasks = [[19,13],[16,9],[21,10],[32,25],[37,4],[49,24],[2,15],[38,41],[37,34],[33,6],[45,4],[18,18],[46,39],[12,24]]
tasks = [[35,36],[11,7],[15,47],[34,2],[47,19],[16,14],[19,8],[7,34],[38,15],[16,18],[27,22],[7,15],[43,2],[10,5],[5,4],[3,11]]


solution = Solution()
print(solution.getOrder(tasks))
