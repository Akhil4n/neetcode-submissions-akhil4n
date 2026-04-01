class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        hand.sort()
        freq_map = Counter(hand)
        for h in hand:
            if freq_map[h] == 0:
                continue
            for i in range(1, groupSize):
                curr = h + i
                if freq_map[curr] <= 0:
                    return False
                freq_map[curr] -= 1
            freq_map[h] -= 1

        return True