class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ind = [0] * numCourses
        adjList = defaultdict(list)

        for crs, pre in prerequisites:
            adjList[pre].append(crs)
            ind[crs] += 1

        queue = deque()
        res = []

        for idx, val in enumerate(ind):
            if val == 0:
                queue.append(idx)

        while queue:
            curr = queue.popleft()
            res.append(curr)
            for nei in adjList[curr]:
                ind[nei] -= 1
                if ind[nei] == 0:
                    queue.append(nei)
        return res if len(res) == numCourses else []
            