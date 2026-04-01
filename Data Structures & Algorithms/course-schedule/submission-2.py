class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ind = [0] * numCourses
        res = 0
        reqMap = defaultdict(list)

        for edge in prerequisites:
            pre, course = edge[1], edge[0]
            reqMap[pre].append(course)
            ind[course] += 1

        queue = deque()
        for i, v in enumerate(ind):
            if v == 0:
                queue.append(i)

        while queue:
            curr = queue.popleft()
            res += 1
            for c in reqMap[curr]:
                ind[c] -= 1
                if ind[c] == 0:
                    queue.append(c)
        
        return res == numCourses