class TimeMap:

    def __init__(self):
        self.key_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_map or timestamp < self.key_map[key][0][0]:
            return ""
        vals = self.key_map[key]
        l, r = 0, len(vals) - 1
        while l < r:
            m = (l + r + 1) // 2
            if vals[m][0] <= timestamp:
                l = m
            else:
                r = m - 1
        return vals[l][1]
