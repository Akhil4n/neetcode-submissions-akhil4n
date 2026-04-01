class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inc = [0] * numCourses
        adj = defaultdict(list)
        for pair in prerequisites:
            pre, crs = pair[1], pair[0]
            inc[crs] += 1
            adj[pre].append(crs)
        
        queue = deque()
        res = 0
        for i, v in enumerate(inc):
            if v == 0:
                queue.append(i)
        while queue:
            res += 1
            curr = queue.popleft()
            for crs in adj[curr]:
                inc[crs] -= 1
                if inc[crs] == 0:
                    queue.append(crs)
            
        return res == numCourses