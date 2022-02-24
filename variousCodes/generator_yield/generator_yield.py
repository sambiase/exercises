def yield_example():
    for i in range(5):
        yield print(i)


next(yield_example())
