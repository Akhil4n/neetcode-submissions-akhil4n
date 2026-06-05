class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []
        count = defaultdict(int)
        l, r = 0, k - 1
        res = []
        for i in range(k):
            heapq.heappush(maxHeap, -1 * nums[i])
            count[nums[i]] += 1
        res.append(maxHeap[0] * -1)
        while r < len(nums) - 1:
            r += 1
            count[nums[r]] += 1
            heapq.heappush(maxHeap, -1 * nums[r])
            count[nums[l]] -= 1
            l += 1
            while count[maxHeap[0] * -1] <= 0:
                heapq.heappop(maxHeap)
            res.append(maxHeap[0] * -1)
        return res
            