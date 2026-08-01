class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        max_pack, weight_sum = 0, 0
        for w in weights:
            max_pack = max(max_pack, w)
            weight_sum += w

        l, r = max_pack, weight_sum 

        def day_count(cap: int) -> int:
            days = 1
            curr = weights[0]
            for i in range(1, len(weights)):
                w = weights[i]
                if curr + w > cap:
                    curr = w
                    days += 1
                else:
                    curr += w
            return days


        while l < r:
            m = (l + r) // 2
            min_days = day_count(m)
            print(m, min_days)
            if min_days > days:
                l = m + 1
            else:
                r = m

        return l