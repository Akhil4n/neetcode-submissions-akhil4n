class FreqStack:

    # 2 steps per pop, find highest freq elem(s), if multiple remove one closest to top
    # issues: store max freq effeciently, remove efficiently

    def __init__(self):
        self.stack = []
        self.counter = defaultdict(int)

    def push(self, val: int) -> None:
        self.stack.append(val)        
        self.counter[val] += 1

    def pop(self) -> int:
        most_freq = set()
        max_val = float('-inf')
        for k, v in self.counter.items():
            max_val = max(max_val, v)
        for k, v in self.counter.items():
            if v == max_val:
                most_freq.add(k)

        for i in range(len(self.stack) - 1, -1, -1):
            val = self.stack[i]
            if val in most_freq:
                self.counter[val] -= 1
                self.stack = self.stack[:i] + self.stack[i + 1:]
                return val



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()