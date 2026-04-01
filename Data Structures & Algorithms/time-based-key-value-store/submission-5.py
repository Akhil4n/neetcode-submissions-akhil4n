class TimeMap:

    def __init__(self):
        self.tMap = {}
        self.lTimes = defaultdict(list)
    def set(self, key: str, value: str, timestamp: int) -> None:
        tKey = (key, timestamp)
        self.tMap[tKey] = value
        self.lTimes[key].append(timestamp)
    def get(self, key: str, timestamp: int) -> str:
        if (key, timestamp) in self.tMap:
            return self.tMap[(key, timestamp)]
        elif key in self.lTimes and timestamp > self.lTimes[key][0]:
            check = self.lTimes[key]
            l, r = 0, len(check) - 1
            while l < r:
                m = (l + r) // 2
                val = check[m]
                if timestamp > val:
                    l = m + 1
                else:
                    r = m - 1
            if check[l] > timestamp:
                l -= 1
            return self.tMap[(key, check[l])]
        return ""
