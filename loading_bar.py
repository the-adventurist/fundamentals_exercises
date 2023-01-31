def loading_bar(n):
    loading_process = ''
    if n < 100:
        loading_process = f'{n}% [{n // 10 * "%"}{(10 - n // 10) * "."}]' + '\n' + 'Still loading...'
    else:
        loading_process = '100% Complete!' + '\n' + f'[{n // 10 * "%"}{(10 - n // 10) * "."}]'
    return loading_process


print(loading_bar(int(input())))
