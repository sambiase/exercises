def yield_example():
    for i in range(5):
        yield i


gen = yield_example()
next(gen)
