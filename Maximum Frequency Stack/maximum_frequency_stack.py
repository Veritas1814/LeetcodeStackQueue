from collections import deque
class FreqStack:
    def __init__(self):
        self.freq_store = {}
        self.all = {}
        self.max_freq = 0
    def push(self, val: int) -> None:
        if val not in self.freq_store:
            self.freq_store[val] = 0
        self.freq_store[val] += 1
        freq = self.freq_store[val]
        self.max_freq = max(self.max_freq, freq)
        if freq not in self.all:
            self.all[freq] = deque()
        self.all[freq].append(val)
    def pop(self) -> int:
        if self.max_freq == 0:
            return None
        val = self.all[self.max_freq].pop()
        self.freq_store[val] -= 1
        if not self.all[self.max_freq]:
            self.max_freq -= 1
        return val
