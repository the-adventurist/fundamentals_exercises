rows = int(input())

field = []

for _ in range(rows):
    line = input().split()
    field.append(line)

connected_dots_sets = [0] * rows
group = 1
for r in range(len(field)):
    for c in range(len(field[r])):
        if field[r][c] == '.':
            connected_dots_sets[group - 1] += 1
            field[r][c] = group
            if c - 1 >= 0:
                if field[r][c - 1]