class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        comp = [0, 0, 0]

        for trip in triplets:
            matches = []
            canSwap = True
            for i, elem in enumerate(trip):
                if elem > target[i]:
                    canSwap = False
                    break
                if elem == target[i]:
                    matches.append(i)
            
            if canSwap:
                if len(matches) > 0:
                    for i in range(3):
                        comp[i] = max(comp[i], trip[i])

        for i, c in enumerate(comp):
            if c != target[i]:
                return False
        return True