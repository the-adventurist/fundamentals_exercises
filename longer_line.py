from math import floor, sqrt


def distance(x1,y1, x2, y2):
    current_distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return current_distance


x_1_first_line = float(input())
y_1_first_line = float(input())
x_2_first_line = float(input())
y_2_first_line = float(input())
x_1_second_line = float(input())
y_1_second_line = float(input())
x_2_second_line = float(input())
y_2_second_line = float(input())

first_line_length = distance(int(x_1_first_line), int(y_1_first_line), int(x_2_first_line), int(y_2_first_line))
second_line_length = distance(int(x_1_second_line), int(y_1_second_line), int(x_2_second_line), int(y_2_second_line))
coordinates_first_line_first_point = abs(int(x_1_first_line)) + abs(int(y_1_first_line))
coordinates_first_line_second_point = abs(int(x_2_first_line)) + abs(int(y_2_first_line))
coordinates_second_line_first_point = abs(int(x_1_second_line)) + abs(int(y_1_second_line))
coordinates_second_line_second_point = abs(int(x_2_second_line)) + abs(int(y_2_second_line))
if first_line_length >= second_line_length:
    if coordinates_first_line_first_point <= coordinates_first_line_second_point:
        print(f'({int(x_1_first_line)}, {int(y_1_first_line)})({int(x_2_first_line)}, {int(y_2_first_line)}')
    else:
        print(f'({int(x_2_first_line)}, {int(y_2_first_line)})({int(x_1_first_line)}, {int(x_1_first_line)})')
else:
    if coordinates_second_line_first_point <= coordinates_second_line_second_point:
        print(f'({int(x_1_second_line)}, {int(y_1_second_line)})({int(x_2_second_line)}, {int(y_2_second_line)})')
    else:
        print(f'({int(x_2_second_line)}, {int(y_2_second_line)})({int(x_1_second_line)}, {int(y_1_second_line)})')
