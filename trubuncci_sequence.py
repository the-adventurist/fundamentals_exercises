def tribonacci_sequence(n):
    trib_sequence = []
    for i in range(0, n):
        if i == 0:
            trib_sequence.append(i + 1)
        elif i == 1:
            trib_sequence.append(i)
        elif i == 2:
            trib_sequence.append(i)
        else:
            current_number = trib_sequence[i - 3] + trib_sequence[i - 2] + trib_sequence[i - 1]
            trib_sequence.append(current_number)
    return trib_sequence


number = int(input())
tribonacci_ = tribonacci_sequence(number)
print(' '.join([str(x) for x in tribonacci_]))
