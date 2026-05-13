class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min1 = 0
        min2 = 0
        for i in range(2, len(cost) + 1):
            temp = min2
            if min1 + cost[i - 2] < min2 + cost[i - 1]:
                min2 = min1 + cost[i - 2]
            else:
                min2 = min2 + cost[i - 1]
            min1 = temp

        return min2