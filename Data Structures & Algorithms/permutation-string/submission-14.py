from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        cnt1 = Counter(s1)
        cnt2 = Counter()
        matches = 0

        # Build first window from s2
        for i in range(len(s1)):
            cnt2[s2[i]] += 1

        # Count initial matches
        for c in cnt1:
            if cnt1[c] == cnt2[c]:
                matches += 1

        if matches == len(cnt1):
            return True

        # Slide window
        for i in range(len(s1), len(s2)):
            right_char = s2[i]
            left_char = s2[i - len(s1)]

            # Add right char
            cnt2[right_char] += 1
            if right_char in cnt1:
                if cnt2[right_char] == cnt1[right_char]:
                    matches += 1
                elif cnt2[right_char] == cnt1[right_char] + 1:
                    matches -= 1

            # Remove left char
            cnt2[left_char] -= 1
            if left_char in cnt1:
                if cnt2[left_char] == cnt1[left_char]:
                    matches += 1
                elif cnt2[left_char] == cnt1[left_char] - 1:
                    matches -= 1

            if matches == len(cnt1):
                return True

        return False
