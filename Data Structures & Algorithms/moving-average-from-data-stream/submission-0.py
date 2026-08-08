class MovingAverage:

    def __init__(self, size: int):
        self.added = 0
        self.size = size
        self.stack = []

    def next(self, val: int) -> float:
        self.added += val
        self.stack.append(val)
        if len(self.stack) > self.size:
            num = self.stack.pop(0)
            self.added -= num
        return self.added / len(self.stack)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
