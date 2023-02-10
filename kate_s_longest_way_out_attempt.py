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

moves_by_routes = []
routes = ['k', '#']
curr_pos_r = k_position_r
curr_pos_c = k_position_c
zz = 0
while True:
    mark_letter = chr(97 + zz)
    routes.append(mark_letter)
    moves_by_routes.append(0)
    while True:
        if (matrix[curr_pos_r][curr_pos_c + 1]) not in routes:
            matrix[curr_pos_r][curr_pos_c + 1] += mark_letter
            curr_pos_c += 1
            moves_by_routes[-1] += 1
            if matrix[curr_pos_r][curr_pos_c + 1] == 'o':
                moves_by_routes[-1] += 1
                break
        elif (matrix[curr_pos_r][curr_pos_c - 1]) not in routes:
            matrix[curr_pos_r][curr_pos_c - 1] += mark_letter
            curr_pos_c -= 1
            moves_by_routes[-1] += 1
            if matrix[curr_pos_r][k_position_c - 1] == 'o':
                moves_by_routes[-1] += 1
                break
        elif (matrix[curr_pos_r - 1][curr_pos_c]) not in routes:
            matrix[curr_pos_r - 1][curr_pos_c] += mark_letter
            curr_pos_r -= 1
            moves_by_routes[-1] += 1
            if matrix[curr_pos_r - 1][curr_pos_c] == 'o':
                moves_by_routes[-1] += 1
                break
        elif (matrix[curr_pos_r + 1][curr_pos_c]) not in routes:
            matrix[curr_pos_r + 1][k_position_c] += mark_letter
            curr_pos_r += 1
            moves_by_routes[-1] += 1
            if matrix[curr_pos_r + 1][curr_pos_c] == 'o':
                moves_by_routes[-1] += 1
                break
        else:
            print('Kate cannot get out')
            exit()
    zz += 1
print(f'Kate got out in {moves} moves')
# This task is not sent to the judge!
