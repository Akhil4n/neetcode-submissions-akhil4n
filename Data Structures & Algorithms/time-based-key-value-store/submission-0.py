class TimeMap:

    def __init__(self):
        self.tMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        tKey = (key, timestamp)
        self.tMap[tKey] = value

    def get(self, key: str, timestamp: int) -> str:
        if (key, timestamp) in self.tMap:
            return self.tMap[(key, timestamp)]
        else:
            v = timestamp
            for i in range(v-1, 0, -1):
                if (key, i) in self.tMap:
                    return self.tMap[(key, i)]
        return ""
