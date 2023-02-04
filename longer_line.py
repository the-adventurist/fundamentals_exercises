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

first_line_length = distance(x_1_first_line, y_1_first_line, x_2_first_line, y_2_first_line)
second_line_length = distance(x_1_second_line, y_1_second_line, x_2_second_line, y_2_second_line)
if first_line_length >= second_line_length:
    first_case_distance = distance(x_1_first_line, y_1_first_line, 0, 0)
    second_case_distance = distance(x_2_first_line, y_2_first_line, 0, 0)
    if first_case_distance < second_case_distance:
        print(f'({x_1_first_line}, {y_1_first_line})({x_2_first_line}, {y_2_first_line}')
    else:
        print(f'({x_2_first_line}, {y_2_first_line})({x_1_first_line}, {x_1_first_line})')
else:
    first_case_distance = distance(x_1_second_line, y_1_second_line, 0, 0)
    second_case_distance = distance(x_2_second_line, y_2_second_line, 0, 0)
    if first_case_distance < second_case_distance:
        print(f'({floor(x_1_second_line)}, {floor(y_1_second_line)})({floor(x_2_second_line)}, {floor(y_2_second_line)})')
    else:
        print(f'({floor(x_2_second_line)}, {floor(y_2_second_line)})({floor(x_1_second_line)}, {floor(y_1_second_line)})')
