class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = defaultdict(list)
        for i in range(len(equations)):
            val, num_1, num_2 = values[i], equations[i][0], equations[i][1]
            adjList[num_1].append((val, num_2))
            adjList[num_2].append((1 / val, num_1))

        def bfs(num_1, num_2) -> int:
            if num_1 not in adjList or num_2 not in adjList:
                return -1
            queue = deque()
            queue.append((1, num_1))
            seen = {num_1}
            while queue:
                curr_div, val = queue.popleft()
                if val == num_2:
                    return curr_div
                for nei in adjList[val]:
                    mult, nxt_val = nei
                    if nxt_val in seen:
                        continue
                    seen.add(nxt_val)
                    queue.append((curr_div * mult, nxt_val))

            return -1

        cache = {}
        res = []
        for start, end in queries:
            if (start, end) in cache:
                res.append(cache[(start, end)])
                continue
            if (end, start) in cache:
                res.append(1 / cache[(end, start)])
                continue
            val = bfs(start, end)
            cache[(start, end)] = val
            res.append(val)
        return res