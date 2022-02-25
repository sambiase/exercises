# Infinite loop with yield


def infinite_loop():
    num = 0
    while True:
        yield print(f'Num {num}')
        num +=1


gen_infinite_loop = infinite_loop()
next(gen_infinite_loop)