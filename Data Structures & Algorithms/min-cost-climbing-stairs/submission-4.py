class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost[0], cost[1])
        cost1, cost2 = cost[0], cost[1]
        for i in range(2, len(cost)):
            temp = min(cost1, cost2)
            cost1 = cost2
            cost2 = temp + cost[i]

        return min(cost1, cost2)