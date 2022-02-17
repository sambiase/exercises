# example usage of *args and **kwargs together


def args_and_kwargs(*args, **kwargs):
    print(f'Args: {args}')
    print(f'Kwargs: {kwargs}')


if __name__ == '__main__':
    args_and_kwargs(3, 4, 5, time='Flamengo', cidade='Rio')
