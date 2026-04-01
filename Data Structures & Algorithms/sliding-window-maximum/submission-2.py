class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []

        l = 0
        r = k - 1
        for i in range(k - 1):
            heapq.heappush(heap, nums[i] * -1)
        freq = Counter(nums)

        while r < len(nums):
            heapq.heappush(heap, nums[r] * -1)
            curMax = heap[0] * -1
            res.append(curMax)
            freq[nums[l]] -= 1
            if nums[l] == curMax:
                heapq.heappop(heap)
            if freq[nums[l]] == 0:
                while heap and nums[l] == heap[0] * -1:
                    heapq.heappop(heap)
            l += 1
            r += 1

        return res
