def dekor(fun):
    def wrapper(x):
        for i in range(8):
            x = fun(x)
        return x
    return wrapper


@dekor
def f(x):
    return x ** 2


print(f(2))
