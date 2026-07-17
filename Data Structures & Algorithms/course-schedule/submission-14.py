class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inc = [0] * numCourses
        adjList = defaultdict(list)

        for crs, pre in prerequisites:
            adjList[pre].append(crs)
            inc[crs] += 1

        res = 0
        queue = deque()
        for i, v in enumerate(inc):
            if v == 0:
                queue.append(i)

        while queue:
            curr = queue.popleft()
            res += 1
            for crs in adjList[curr]:
                inc[crs] -= 1
                if inc[crs] == 0:
                    queue.append(crs)

        return res == numCourses