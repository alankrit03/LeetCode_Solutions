class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = [0] * maxSize
        self.maxSize = maxSize
        self.top = -1
        self.rear = 0

    def __isfull(self):
        if self.top == self.maxSize - 1:
            return True

    def __isempty(self):
        if self.top == self.rear - 1:
            return True

    def push(self, x: int) -> None:
        if not self.__isfull():
            self.top += 1
            self.stack[self.top] = x

    def pop(self) -> int:
        if not self.__isempty():
            self.top -= 1
            return self.stack[self.top + 1]
        return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, self.top + 1)):
            self.stack[i] += val

# Your CustomStack object will be instantiated and called as such:
obj = CustomStack(10)
print(obj.pop())
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)