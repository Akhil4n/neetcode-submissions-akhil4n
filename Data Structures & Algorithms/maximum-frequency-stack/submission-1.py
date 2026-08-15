class FreqStack:

    # 2 steps per pop, find highest freq elem(s), if multiple remove one closest to top
    # issues: store max freq effeciently, remove efficiently

    def __init__(self):
        self.counter = defaultdict(int)
        self.mf = 0
        self.count_map = defaultdict(list)

    def push(self, val: int) -> None:
        count = self.counter[val]
        new_count = count + 1

        if new_count > self.mf:
            self.mf = new_count

        self.count_map[new_count].append(val)
        self.counter[val] += 1
        
    def pop(self) -> int:
        val = self.count_map[self.mf].pop()
        while self.counter[val] != self.mf:
            val = self.count_map[self.mf].pop()
        if len(self.count_map[self.mf]) == 0:
            self.mf -= 1
        self.counter[val] -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()