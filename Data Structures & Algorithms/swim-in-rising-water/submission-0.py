class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        seen = set()
        heap = []
        maxTime = grid[0][0]
        heap.append((grid[0][0], 0, 0))
        while heap:
            val, r, c = heapq.heappop(heap)
            maxTime = max(maxTime, val)
            if r == rows - 1 and c == cols - 1:
                break
            for d in dirs:
                newI, newJ = r + d[0], c + d[1]
                if min(newI, newJ) < 0 or newI >= rows or newJ >= cols or (newI, newJ) in seen:
                    continue
                heapq.heappush(heap, (grid[newI][newJ], newI, newJ))
            seen.add((r, c))

        return maxTime


        

        
