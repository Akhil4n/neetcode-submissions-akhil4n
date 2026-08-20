class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(l, r):
            if l >= r:
                return
            partition = (l + r) // 2
            pivot = nums[partition]
            nums[l], nums[partition] = pivot, nums[l]
            i, j = l + 1, r
            while i <= j:
                while i <= j and nums[i] <= pivot:
                    i += 1
                while i <= j and nums[j] >= pivot:
                    j -= 1
                if i <= j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -=1

            nums[j], nums[l] = pivot, nums[j]
            quicksort(l, j - 1)
            quicksort(j + 1, r)

        quicksort(0, len(nums) - 1)
        return nums