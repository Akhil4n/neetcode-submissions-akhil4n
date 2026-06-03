class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        comp = [0, 0, 0]

        for trip in triplets:
            if trip[0] <= target[0] and trip[1] <= target[1] and trip[2] <= target[2]:
                for i in range(3):
                    comp[i] = max(comp[i], trip[i])

        return comp == target