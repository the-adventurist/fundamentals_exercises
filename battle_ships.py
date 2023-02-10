rows_number = int(input())

field = []
destroyed_ships = 0

for _ in range(rows_number):
    line = [int(x) for x in input().split()]
    field.append(line)
list_coordinates = input().split()
for pair_coordinates in list_coordinates:
    r_number, c_number = [int(x) for x in pair_coordinates.split('-')]
    if field[r_number][c_number] > 0:
        field[r_number][c_number] -= 1
        if field[r_number][c_number] == 0:
            destroyed_ships += 1
print(destroyed_ships)
# This problem is not sent to the judge !