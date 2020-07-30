def f(a):
    def extend(fuc):
        def hello(*args, **kwargs):
            print(args)
            print(kwargs)
            fuc(*args,**kwargs)
            print(a)
        return hello
    return extend


@f("abcde")
def a():
    print("a")


def test_a():
    a()


