class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        odd_len = curr_odd = 1
        even_len = curr_even = 1

        for i in range(len(arr) - 1):
            val, nxt = arr[i], arr[i + 1]
            if i % 2 == 0:
                if val > nxt:
                    curr_even += 1
                    even_len = max(even_len, curr_even)
                    curr_odd = 1
                elif val < nxt:
                    curr_odd += 1
                    odd_len = max(odd_len, curr_odd)
                    curr_even = 1
            else:
                if val > nxt:
                    curr_odd += 1
                    odd_len = max(odd_len, curr_odd)
                    curr_even = 1
                elif val < nxt:
                    curr_even += 1
                    even_len = max(even_len, curr_even)
                    curr_odd = 1
        odd_len = max(odd_len, curr_odd)
        even_len = max(even_len, curr_even)
        return max(odd_len, even_len)



