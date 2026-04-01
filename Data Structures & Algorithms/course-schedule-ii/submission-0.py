class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        courseMap = defaultdict(list)
        incoming = [0] * (numCourses)
        for p in prerequisites:
            v, k = p[0], p[1]
            courseMap[k].append(v)
            incoming[v] += 1
        queue = deque()
        for i in range(len(incoming)):
            if incoming[i] == 0:
                queue.append(i)
        while queue:
            curr = queue.popleft()
            res.append(curr)
            for c in courseMap[curr]:
                incoming[c] -= 1
                if incoming[c] == 0:
                    queue.append(c)
        print(res)
        return res if len(res) == numCourses else []
