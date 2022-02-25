def multi_yield():
        name = 'First name'
        yield name
        name = 'Second name'
        yield name


multi_yield_obj = multi_yield()
print(next(multi_yield_obj))