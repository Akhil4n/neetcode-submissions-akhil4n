class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = fresh = 0
        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                curr = grid[i][j]
                if curr == 2:
                    queue.append((i, j))
                elif curr == 1:
                    fresh += 1

        while queue and fresh > 0:
            time += 1
            for i in range(len(queue)):
                r, c = queue.popleft()

                if r + 1 < len(grid) and grid[r + 1][c] == 1:
                    fresh -= 1
                    queue.append((r + 1, c))
                    grid[r + 1][c] = 2

                if r - 1 >= 0 and grid[r - 1][c] == 1:
                    fresh -= 1
                    queue.append((r - 1, c))
                    grid[r - 1][c] = 2

                if c + 1 < len(grid[0]) and grid[r][c + 1] == 1:
                    fresh -= 1
                    queue.append((r, c + 1))
                    grid[r][c + 1] = 2

                if c - 1 >= 0 and grid[r][c - 1] == 1:
                    fresh -= 1
                    queue.append((r, c - 1))
                    grid[r][c - 1] = 2

        return time if fresh == 0 else -1
