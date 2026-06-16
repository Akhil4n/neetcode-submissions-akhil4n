class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ind = [0] * numCourses
        preMap = defaultdict(list)
        queue = deque()

        for crs, pre in prerequisites:
            ind[crs] += 1
            preMap[pre].append(crs)
        
        for i, v in enumerate(ind):
            if v == 0:
                queue.append(i)
        
        comp = 0
        while queue:
            curr = queue.popleft()
            comp += 1
            if comp == numCourses:
                return True
            for crs in preMap[curr]:
                ind[crs] -= 1
                if ind[crs] == 0:
                    queue.append(crs)

        return False