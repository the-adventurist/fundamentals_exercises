def cast_data_type(type_data, data_):
    if type_data == 'string':
        return f'${data_}$'
    elif type_data == 'int':
        data_ = int(data_)
        return data_ * 2
    else:
        data_ = float(data_)
        return f'{data_ * 1.5:.2f}'


print(cast_data_type(input(), input()))
