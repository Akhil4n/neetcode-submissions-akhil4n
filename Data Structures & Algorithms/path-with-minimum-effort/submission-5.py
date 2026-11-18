class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        seen = set()
        heap = [(0, 0, 0)] # holds effort, x, y
        dirs = {(0, 1), (0, -1), (1, 0), (-1, 0)}
        while heap:
            effort, r, c = heapq.heappop(heap)
            if (r, c) in seen:
                continue
            if r == rows - 1 and c == cols - 1:
                return effort
            seen.add((r, c))
            val = heights[r][c]
            for add_r, add_c in dirs:
                row, col = r + add_r, c + add_c
                if min(row, col) < 0 or row >= rows or col >= cols or (row, col) in seen:
                    continue
                curr_effort = max(effort, abs(val - heights[row][col]))
                heapq.heappush(heap, (curr_effort, row, col))
        return 0




