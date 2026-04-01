class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        costs = {0: cost[0], 1: cost[1]}
        prev, curr = costs[0], costs[1]
        for i in range(2, len(cost)):
            new = min(prev, curr) + cost[i]
            prev = curr
            curr = new
        return min(prev, curr)
        
