# example usage of **kwargs


def nomes(**kwargs):
    print(f'Nome: {kwargs.values()}')
    print(f'Tipo do kwargs {type(kwargs)}')


if __name__ == '__main__':

    nomes(first_name='Andre', last_name='Silva')
