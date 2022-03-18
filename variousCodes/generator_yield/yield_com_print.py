
def print_times():
    yield print('Fla')
    yield print('Mengo')


gen = print_times()
next(gen)
