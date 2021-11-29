class Pan:
    def __init__(self):
        self.list = [0, 1, 1, 2, 4]
        self.current = 0
        self.call = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.call < 5:
            self.call += 1
            return self.list[self.call-1]
        temporary = 0
        for i in range(5):
            temporary += self.list[self.current]
            self.current += 1
            if self.current > 4:
                self.current = 0
        self.list[self.current] = temporary
        self.current += 1
        return temporary


p = Pan()
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
