def dekor(fun):
    def wrapper(x):
        return fun(fun(x))

    return wrapper


@dekor
def f(x):
    return x ** 2


print(f(2))
