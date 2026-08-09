class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heap = []
        seen = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(heights), len(heights[0])

        heap.append((0, 0, 0))
        while heap:
            effort, r, c = heapq.heappop(heap)
            height = heights[r][c]
            if r == rows - 1 and c == cols - 1:
                return effort
            if (r, c) in seen:
                continue
            seen.add((r, c))
            for d in dirs:
                x, y = r + d[0], c + d[1]
                if min(x, y) < 0 or x >= rows or y >= cols or (x, y) in seen:
                    continue
                curr_eff = abs(height - heights[x][y])
                heapq.heappush(heap, (max(effort, curr_eff), x, y))
