class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        time = 0
        fresh = 0
        queue = deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        dirs = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        while queue:
            time += 1
            for i in range(len(queue)):
                curr = queue.popleft()
                for dr in dirs:
                    crds = (curr[0] + dr[0], curr[1] + dr[1])
                    if min(crds[0], crds[1]) < 0 or crds[0] >= rows or crds[1] >= cols or grid[crds[0]][crds[1]] != 1:
                        continue
                    grid[crds[0]][crds[1]] = 2
                    fresh -= 1
                    if fresh == 0:
                        return time
                    queue.append(crds)

        return time if fresh == 0 else -1








