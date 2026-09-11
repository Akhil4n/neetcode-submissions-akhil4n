class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, k - 1
        resl, resr = l, r
        dist = 0
        for i in range(r + 1):
            dist += abs(arr[i] - x)
        
        cdist = dist
        for j in range(r + 1, len(arr)):
            curr = arr[j]
            cdist -= abs(arr[l] - x)
            l += 1
            cdist += abs(curr - x)
            if cdist < dist:
                resl, resr = l, j
            dist = min(dist, cdist)

        return arr[resl: resr + 1]