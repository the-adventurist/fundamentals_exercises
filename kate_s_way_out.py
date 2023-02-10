number_of_rows = int(input())
matrix = []

k_position_r = 0
k_position_c = 0
moves = 0
for _ in range(number_of_rows):
    line = [x for x in input()]
    line.insert(0, 'o')
    line.append('o')
    matrix.append(line)
matrix.insert(0, ['o'] * len(matrix[0]))
matrix.append(['o'] * len(matrix[0]))

for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        if matrix[r][c] == 'k':
            k_position_r = r
            k_position_c = c


while True:
    if matrix[k_position_r][k_position_c + 1] == ' ':
        matrix[k_position_r][k_position_c + 1] = 'k'
        k_position_c += 1
        moves += 1
        if matrix[k_position_r][k_position_c + 1] == 'o':
            moves += 1
            break
    elif matrix[k_position_r][k_position_c - 1] == ' ':
        matrix[k_position_r][k_position_c - 1] = 'k'
        k_position_c -= 1
        moves += 1
        if matrix[k_position_r][k_position_c - 1] == 'o':
            moves += 1
            break
    elif matrix[k_position_r - 1][k_position_c] == ' ':
        matrix[k_position_r - 1][k_position_c] = 'k'
        k_position_r -= 1
        moves += 1
        if matrix[k_position_r - 1][k_position_c] == 'o':
            moves += 1
            break
    elif matrix[k_position_r + 1][k_position_c] == ' ':
        matrix[k_position_r + 1][k_position_c] = 'k'
        k_position_r += 1
        moves += 1
        if matrix[k_position_r + 1][k_position_c] == 'o':
            moves += 1
            break
    else:
        print('Kate cannot get out')
        exit()
print(f'Kate got out in {moves} moves')
# This task is not sent to the judge!
