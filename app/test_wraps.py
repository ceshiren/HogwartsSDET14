def f(a):
    def extend(fuc):
        def hello(*args, **kwargs):
            print(args)
            print(kwargs)
            fuc(*args, **kwargs)
            print(a)

        return hello

    return extend


@f("xxxxx")
def a():
    print("a")


def test_a():
    a()


def test_xx():
    a = {"a": {"c": 20}, "b": 20}

    def c(b, a):
        print(a, b)

    c(**a)
