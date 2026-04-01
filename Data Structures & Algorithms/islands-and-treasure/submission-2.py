from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def bfs(i, j, seen):
            level = 1
            queue = deque([[i, j]])
            while len(queue) > 0:
                n = len(queue)
                for i in range(n):
                    coords = queue.pop()
                    seen.add((coords[0], coords[1]))
                    row, col = coords[0], coords[1]
                    if row < len(grid) - 1 and grid[row + 1][col] > 0 and (row + 1, col) not in seen:
                        grid[row + 1][col] = min(level, grid[row + 1][col])
                        queue.appendleft([row+1, col])
                    if row > 0 and grid[row - 1][col] > 0 and (row - 1, col) not in seen:
                        grid[row - 1][col] = min(level, grid[row - 1][col])
                        queue.appendleft([row - 1, col])
                    if col < len(grid[0]) - 1 and grid[row][col + 1] > 0 and (row, col + 1) not in seen:
                        grid[row][col + 1] = min(level, grid[row][col + 1])
                        queue.appendleft([row, col + 1])
                    if col > 0 and grid[row][col - 1] > 0 and (row, col - 1) not in seen:
                        grid[row][col - 1] = min(level, grid[row][col - 1])
                        queue.appendleft([row, col - 1])
                level += 1
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    seen = set()
                    bfs(i, j, seen)
