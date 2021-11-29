class decorator:
    def __init__(self, fun):
        self.fun = fun
        self.dictionary = {}

    def __iter__(self):
        return self

    def __call__(self, *args, **kwargs):
        print("Call")
        if args[0] not in self.dictionary:
            self.dictionary[args[0]] = self.fun(args[0])
        return self.dictionary[args[0]]


@decorator
def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


print(Fibonacci(6))
print(Fibonacci.dictionary)
