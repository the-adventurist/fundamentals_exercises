n = 3
matrix = []
for _ in range(3):
    row = input()
    line = []
    for symbol in row:
        if symbol != ' ':
            line.append(symbol)
    matrix.append(line)
for