class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        cmap = defaultdict(list)
        indegree = [0] * numCourses
        for c, pr in prerequisites:
            cmap[pr].append(c)
            indegree[c] += 1
        queue = deque([])
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        taken = 0
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                for c in cmap[curr]:
                    indegree[c] -= 1
                    if indegree[c] == 0:
                        queue.append(c)
                taken += 1
        return True if taken == numCourses else False