class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        perimeter = sum(matchsticks)
        if perimeter % 4 != 0:
            return False
        sl = perimeter // 4
        matchsticks.sort(reverse=True)

        def find_square(i, left, right, top, bottom):
            if i >= len(matchsticks):
                if sl == left and (left == right and right == top and top == bottom):
                    return True
                return False

            match = matchsticks[i]
            if match > sl:
                return False
            if left + match <= sl:
                if find_square(i + 1, left + match, right, top, bottom):
                    return True
            if right + match <= sl:
                if find_square(i + 1, left, right + match, top, bottom):
                    return True
            if top + match <= sl:
                if find_square(i + 1, left, right, top + match, bottom):
                    return True
            if bottom + match <= sl:
                if find_square(i + 1, left, right, top, bottom + match):
                    return True
            return False

        return find_square(0, 0, 0, 0, 0)