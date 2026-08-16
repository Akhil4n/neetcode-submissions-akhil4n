class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort()
        i = 0
        time = tasks[i][0]
        heap = []
        res = []
        while i < len(tasks) and tasks[i][0] == time:
            heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
            i += 1
        while len(res) < len(tasks):
            if heap:
                curr = heapq.heappop(heap)
                res.append(curr[1])
                time += curr[0]
            else:
                time = tasks[i][0]

            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1

        return res
