from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        numFresh = 0
        stack = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                val = grid[i][j]
                if val == 1:
                    numFresh += 1
                elif val == 2:
                    stack.append([i, j])
        while stack and numFresh > 0:
            time += 1
            start = len(stack)
            print(start)
            print(stack)
            for i in range(start):
                vals = stack.popleft()
                row, col = vals[0], vals[1]
                if row + 1 < len(grid) and grid[row + 1][col] == 1:
                    numFresh -= 1
                    grid[row + 1][col] = 2
                    stack.append([row + 1, col])
                if row - 1 >= 0 and grid[row - 1][col] == 1:
                    numFresh -= 1
                    grid[row - 1][col] = 2
                    stack.append([row - 1, col])
                if col - 1 >= 0 and grid[row][col - 1] == 1:
                    numFresh -= 1
                    grid[row][col - 1] = 2
                    stack.append([row, col - 1])
                if col + 1 < len(grid[0]) and grid[row][col + 1] == 1:
                    numFresh -= 1
                    grid[row][col + 1] = 2
                    stack.append([row, col + 1])
        print(numFresh)
        if numFresh > 0:
            return -1
        return time
