def repeat(times):
    def wrapper(fun):
        def inner_wrapper(x):
            f = fun(x)
            for i in range(times):
                f = fun(x)
            return f

        return inner_wrapper

    return wrapper


def f(x):
    return x ** 2


f3 = repeat(3)(f)
print(f3(2))
