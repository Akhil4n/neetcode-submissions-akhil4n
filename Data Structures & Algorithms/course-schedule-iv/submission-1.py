class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        ind = [0] * numCourses
        prereqs = [set() for _ in range(numCourses)]
        adjList = defaultdict(list)
        queue = deque()

        for pre, crs in prerequisites:
            ind[crs] += 1
            adjList[pre].append(crs)

        for crs, val in enumerate(ind):
            if val == 0:
                queue.append(crs)

        while queue:
            curr = queue.popleft()
            curr_pres = prereqs[curr]
            for crs in adjList[curr]:
                prereqs[crs].update(curr_pres)
                prereqs[crs].add(curr)
                ind[crs] -= 1
                if ind[crs] == 0:
                    queue.append(crs)

        res = []
        for pre, crs in queries:
            res.append(pre in prereqs[crs])

        return res
