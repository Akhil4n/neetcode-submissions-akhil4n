import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(l, r):
            if l >= r:
                return
            rand_idx = random.randint(l, r)
            nums[rand_idx], nums[r] = nums[r], nums[rand_idx]
            partition = r
            pivot = nums[partition]
            i = j = l
            while j < r:
                while j < r and nums[j] > pivot:
                    j += 1
                if j < r and i < r:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j += 1
            nums[i], nums[r] = nums[r], nums[i]
            quicksort(l, i - 1)
            quicksort(i + 1, r)

        quicksort(0, len(nums) - 1)
        return nums