def search_engine(first, second, third):
    if first < second and first < third:
        return first
    elif second < first and second < third:
        return second
    return third


print(search_engine(int(input()), int(input()), int(input())))
