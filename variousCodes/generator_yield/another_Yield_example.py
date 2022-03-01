import time

def multi_yield():
        time.sleep(5) # sleeps for 5 segs before continuing
        name = 'First name'
        yield name
        name = 'Second name'
        yield name


multi_yield_obj = multi_yield()
print(next(multi_yield_obj))